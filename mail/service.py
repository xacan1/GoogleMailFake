from mail.models import *
from django.db.models import Q


def have_chain(email_pk: int) -> bool:
    result = False
    queryset = Email.objects.filter(parent=email_pk)

    if queryset.exists():
        result = True
        return result

    queryset = Email.objects.filter(pk=email_pk)

    if queryset.exists():
        email = queryset.first()

        if email.parent:
            result = True
            return result

    return result


def get_chain(email_pk: int) -> list:
    chain_emails = []
    first_email = get_first_email_in_chain(email_pk)
    next_email = first_email
    chain_emails.append(next_email)

    while next_email:
        queryset = Email.objects.filter(parent=next_email)

        if queryset.exists():
            next_email = queryset.first()
            chain_emails.append(next_email)
        else:
            break

    return chain_emails


def get_first_email_in_chain(email_pk: int):
    first_email = Email.objects.get(pk=email_pk)

    while first_email.parent:
        first_email = Email.objects.get(pk=first_email.parent.pk)

    return first_email


def get_emails_by_category(user, slug: str):
    # user = self.request.user
    # slug = self.kwargs.get('category_slug', '')

    if slug:
        queryset = Email.objects.select_related(
            'category').filter(user=user, category__slug=slug)
    else:
        queryset = Email.objects.filter(user=user)

    return queryset


def simple_search_email(query_search: str):
    queryset = None

    if not query_search:
        return queryset

    queryset = Email.objects.filter(
        Q(subject__icontains=query_search) | Q(body__icontains=query_search) | Q(sender__icontains=query_search) | Q(user__email__icontains=query_search))

    return queryset


def search_email(query_search: str):
    query_search = query_search[0:100]
    search_words = query_search.split(' ', 9)
    q_filter_and = Q()

    for word in search_words:
        if not word:
            continue

        q_filter_or = Q()
        q_filter_or |= Q(subject__icontains=word)
        q_filter_or |= Q(body__icontains=word)
        q_filter_or |= Q(sender__icontains=word)
        q_filter_or |= Q(user__email__icontains=word)
        q_filter_and &= q_filter_or

    queryset = Email.objects.filter(q_filter_and)

    return queryset
