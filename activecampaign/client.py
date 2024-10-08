import requests

from .accounts import Accounts
from .activities import Activities
from .automations import Automations
from .contacts import Contacts
from .deals import Deals
from .deep_data_integrations import DeepDataIntegrations
from .events import Events
from .lists import Lists
from .notes import Notes
from .tasks import Tasks
from .users import Users
from .webhooks import Webhooks
from .messages import Messages
from .tags import Tags
from .email_activities import EmailActivities
from .deal_activities import DealActivities
from .customobjects import CustomObjects
from .campaigns import Campaigns
from .addresses import Addresses
from .brandings import Brandings
from .account_contact import AccountContact


class Client(object):
    BASE_URL = '{}/api/3'

    def __init__(self, url, api_key):
        self.BASE_URL = self.BASE_URL.format(url)
        self.api_key = api_key

        self.accounts = Accounts(self)
        self.account_contact = AccountContact(self)
        self.activities = Activities(self)
        self.automations = Automations(self)
        self.contacts = Contacts(self)
        self.deals = Deals(self)
        self.events = Events(self)
        self.lists = Lists(self)
        self.notes = Notes(self)
        self.tasks = Tasks(self)
        self.users = Users(self)
        self.webhooks = Webhooks(self)
        self.messages = Messages(self)
        self.deepdataintegrations = DeepDataIntegrations(self)
        self.tags = Tags(self)
        self.emailActivities = EmailActivities(self)
        self.dealActivities = DealActivities(self)
        self.customobjects = CustomObjects(self)
        self.campaigns = Campaigns(self)
        self.addresses = Addresses(self)
        self.brandings = Brandings(self)

    def _get(self, endpoint, **kwargs):
        return self._request('GET', endpoint, **kwargs)

    def _post(self, endpoint, **kwargs):
        return self._request('POST', endpoint, **kwargs)

    def _put(self, endpoint, **kwargs):
        return self._request('PUT', endpoint, **kwargs)

    def _delete(self, endpoint, **kwargs):
        return self._request('DELETE', endpoint, **kwargs)

    def _request(self, method, endpoint, headers=None, **kwargs):
        _headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Api-Token': self.api_key
        }
        if headers:
            _headers.update(headers)

        return self._parse(requests.request(method, self.BASE_URL + endpoint, headers=_headers, **kwargs))

    def _parse(self, response):
        if 'application/json' in response.headers['Content-Type']:
            r = response.json()
        else:
            return response.text

        return r
