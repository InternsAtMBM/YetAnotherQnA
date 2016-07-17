from django import template
from forum.models import Question, Answer
register = template.Library()

"""
NOT WORKING

@register.inclusion_tag('forum/question_detail.html', takes_context=True)
def chk_question_vote(context):
    question = context['question']
    request = context['request']
    print "this is special \n\n\n\n"
    print question
    print request.user
    print request.META['HTTP_ADDR']
    print "---------------------------"
    return question.rating.get_rating_for_user(request.user, request.META['REMOTE_ADDR'])

@register.inclusion_tag('forum/question_detail.html', takes_context=True)
def chk_answer_vote(context):
    answer = context['answer']
    request = context['request']
    x = answer.rating.get_rating_for_user(request.user, request.META['REMOTE_ADDR'])
    print x
    return x


"""