from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.db.models import Q
from .models import Participant, CTFQuestion, Flag

def home(request):
    return render(request, 'home.html')

def admin_login(request):
    error = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Updated admin credentials
        if username == 'WopSol' and password == 'Wop!@#123':
            request.session['admin_logged_in'] = True
            return redirect('admin_portal')
        else:
            error = 'Invalid username or password'
    return render(request, 'admin_login.html', {'error': error})

def admin_logout(request):
    request.session.flush()
    return redirect('admin_login')

def participant_login(request):
    error = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            participant = Participant.objects.get(username=username, password=password)
            request.session['participant_logged_in'] = True
            request.session['participant_id'] = username  # Store participant id in session
            return redirect('participant_page')
        except Participant.DoesNotExist:
            error = 'Invalid participant ID or password'
    return render(request, 'participant_login.html', {'error': error})

def admin_portal(request):
    # If user is not logged in, redirect to login
    if not request.session.get('admin_logged_in'):
        return redirect('admin_login')

    from .models import CTFQuestion, Flag, Participant

    if request.method == 'POST':
        # Handle adding new questions, flags, participants
        if 'add_question' in request.POST:
            question_text = request.POST.get('question_text')
            points = request.POST.get('points')
            file = request.FILES.get('file')
            if question_text:
                question = CTFQuestion(question_text=question_text, points=int(points) if points else 0)
                if file:
                    question.file = file
                question.save()
        elif 'add_flag' in request.POST:
            flag_text = request.POST.get('flag_text')
            question_id = request.POST.get('question')
            if flag_text and question_id:
                try:
                    question = CTFQuestion.objects.get(id=question_id)
                    Flag.objects.create(flag_text=flag_text, question=question)
                except CTFQuestion.DoesNotExist:
                    pass
        elif 'add_participant' in request.POST:
            username = request.POST.get('username')
            password = request.POST.get('password')
            if username and password:
                Participant.objects.create(username=username, password=password)
        # Handle editing and deleting questions, flags, and participants
        elif 'edit_question' in request.POST:
            question_id = request.POST.get('edit_question_id')
            question_text = request.POST.get('edit_question_text')
            question_points = request.POST.get('edit_question_points')
            try:
                question = CTFQuestion.objects.get(id=question_id)
                question.question_text = question_text
                question.points = int(question_points) if question_points else 0
                question.save()
            except CTFQuestion.DoesNotExist:
                pass
        elif 'delete_question' in request.POST:
            question_id = request.POST.get('edit_question_id')
            try:
                question = CTFQuestion.objects.get(id=question_id)
                question.delete()
            except CTFQuestion.DoesNotExist:
                pass
        elif 'edit_flag' in request.POST:
            flag_id = request.POST.get('edit_flag_id')
            flag_text = request.POST.get('edit_flag_text')
            try:
                flag = Flag.objects.get(id=flag_id)
                flag.flag_text = flag_text
                flag.save()
            except Flag.DoesNotExist:
                pass
        elif 'delete_flag' in request.POST:
            flag_id = request.POST.get('edit_flag_id')
            try:
                flag = Flag.objects.get(id=flag_id)
                flag.delete()
            except Flag.DoesNotExist:
                pass
        elif 'edit_participant' in request.POST:
            participant_id = request.POST.get('edit_participant_id')
            username = request.POST.get('edit_participant_username')
            password = request.POST.get('edit_participant_password')
            try:
                participant = Participant.objects.get(id=participant_id)
                participant.username = username
                if password:
                    participant.password = password
                participant.save()
            except Participant.DoesNotExist:
                pass
        elif 'delete_participant' in request.POST:
            participant_id = request.POST.get('edit_participant_id')
            try:
                participant = Participant.objects.get(id=participant_id)
                participant.delete()
            except Participant.DoesNotExist:
                pass

    questions = CTFQuestion.objects.all()
    flags = Flag.objects.all()
    participants = Participant.objects.all()
    question_flag_map = {}
    for question in questions:
        question_flag_map[question] = flags.filter(question=question)
    return render(request, 'admin_portal.html', {'question_flag_map': question_flag_map, 'questions': questions, 'participants': participants})

def participant_page(request):
    if not request.session.get('participant_logged_in'):
        return redirect('participant_login')

    participant_username = request.session.get('participant_id')
    participant = None
    message = None

    if participant_username:
        try:
            participant = Participant.objects.get(username=participant_username)
        except Participant.DoesNotExist:
            participant = None

    # Get all questions ordered by creation date or id
    all_questions = CTFQuestion.objects.order_by('id').all()

    # Get solved questions by participant
    solved_questions = participant.solved_questions.all() if participant else []

    # Determine next question to unlock
    next_question = None
    for question in all_questions:
        if question not in solved_questions:
            next_question = question
            break

    # If all questions solved, next_question is None

    if request.method == 'POST':
        question_id = request.POST.get('question_id')
        answer = request.POST.get('answer')
        if question_id and answer:
            try:
                question = CTFQuestion.objects.get(id=question_id)
                flags = Flag.objects.filter(question=question)
                if not flags.exists():
                    message = "No flag found for this question."
                else:
                    # Check if any flag matches the answer
                    correct_flag = False
                    for flag in flags:
                        if flag.flag_text == answer:
                            correct_flag = True
                            break
                    if correct_flag:
                        # Correct answer
                        if participant:
                            if question not in solved_questions:
                                participant.solved_questions.add(question)
                                participant.score += question.points
                                participant.save()
                        message = f"Congratulations! You won {question.points} points."
                        # Update next_question after solving
                        solved_questions = participant.solved_questions.all()
                        next_question = None
                        for q in all_questions:
                            if q not in solved_questions:
                                next_question = q
                                break
                    else:
                        message = "Incorrect answer. Try again."
            except CTFQuestion.DoesNotExist:
                message = "Invalid question selected."

    # Prepare question_files dict for file downloads
    question_files = {q.id: q.file.url if q.file else None for q in all_questions}

    # Only pass the next_question to the template for selection
    questions_to_show = [next_question] if next_question else []

    # Pass the file url of the current question separately for easier access in template
    current_file_url = next_question.file.url if next_question and next_question.file else None

    return render(request, 'participant_page.html', {
        'questions': questions_to_show,
        'participant': participant,
        'message': message,
        'question_files': question_files,
        'current_file_url': current_file_url,
        'all_questions_solved': next_question is None,
    })

def participant_scores(request):
    if not request.session.get('admin_logged_in'):
        return JsonResponse({'error': 'Unauthorized'}, status=401)
    participants = Participant.objects.all().values('username', 'score').order_by('-score')
    return JsonResponse(list(participants), safe=False)

def live_scoreboard(request):
    participants = Participant.objects.all().values('username', 'score').order_by('-score')
    return JsonResponse(list(participants), safe=False)

def live_scoreboard_page(request):
    return render(request, 'live_scoreboard.html')
