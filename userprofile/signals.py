from django.db.models.signals import post_save, post_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import UserProfile, Relationship


@receiver(post_save, sender=User)
def post_save_create_profile(sender, instance, created, **kwargs):
    # print('sender', sender)
    # print('instance', instance)
    if created:  # if user is created
        UserProfile.objects.create(user=instance)
        cur_user = UserProfile.objects.filter(user=instance)[0]
        Relationship.objects.create(sender = cur_user, receiver = cur_user)


@receiver(post_save, sender=Relationship)
def post_save_add_to_friends(sender, instance, created, **kwargs):
    sender_ = instance.sender
    receiver_ = instance.receiver
    #if instance.status == 'accepted':
    # sender_.subscribers.add(receiver_.user)
    # receiver_.subscriptions.add(sender_.user)
    # #sender_.save()
    # receiver_.save()
    # if instance.status == 'send':
    sender_.subscriptions.add(receiver_.user)
    receiver_.subscribers.add(sender_.user)
    sender_.save()
    receiver_.save()



@receiver(post_delete, sender=Relationship)
def post_save_add_to_friends(sender, instance, **kwargs):

    sender_ = instance.sender
    receiver_ = instance.receiver

    sender_.subscriptions.remove(receiver_.user)
    receiver_.subscribers.remove(sender_.user)
    sender_.save()
    receiver_.save()
