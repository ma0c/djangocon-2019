import factory

from applications.events.tests.factories import EventFactory
from applications.tickets.models import Ticket
from applications.users.tests.factories import UserFactory


class TicketFactory(factory.DjangoModelFactory):
    class Meta:
        model = Ticket

    id = factory.Faker('uuid4')
    event = factory.SubFactory(EventFactory)
    user = factory.SubFactory(UserFactory)
