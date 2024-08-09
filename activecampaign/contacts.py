class Contacts(object):
    def __init__(self, client):
        self.client = client

    def create(self, data):
        """
        Create a new contact
        --------------------

        Example:
            data = {
                "contact": {
                    "email": "johndoe@example.com",
                    "firstName": "John",
                    "lastName": "Doe",
                    "phone": "7223224241"
                }
            }
            response = client.contacts.create_contact(data)

        Args:
            data:

        Returns:

        """

        if 'contact' in data:
            contact_data = data
        else:
            contact_data = {
                'contact': data
            }

        response = self.client._post("/contacts", json=contact_data)

        if 'contact' in response:
            return response['contact']
        else:
            return response

    def create_or_update(self, data):
        """
        Create a new contact or update it

        Example:
            data = {
                "email": "johndoe@example.com",
                "firstName": "John",
                "lastName": "Doe",
                "phone": "7223224241",
                "fieldValues": [{
                        "field": "1",
                        "value": "The Value for First Field"
                    },
                    {
                        "field": "6",
                        "value": "2008-01-20"
                    }
                ]
            }
            response = client.contacts.update_contact(data)

        Args:
            data:

        Returns:

        """

        if 'contact' in data:
            contact_data = data
        else:
            contact_data = {
                'contact': data
            }

        response = self.client._post("/contact/sync", json=contact_data)
        if 'contact' in response:
            return response['contact']
        else:
            return response

    def retrieve(self, contact_id):
        """
        Retrieve an existing contact


        Args:
            contact_id:

        Returns:

        """
        return self.client._get("/contacts/{}".format(contact_id))

    def add_to_list(self, list_id, contact_id):
        """
        Add contact to list

        :param list_id:
        :param contact_id:
        :return:
        """

        data = {
            "contactList": {
                "list": list_id,
                "contact": contact_id,
                "status": 1  # 1 - Subscribed, 2 - Unsubscribed
            }
        }

        response = self.client._post("/contactLists", json=data)
        if 'contactList' in response:
            return response['contactList']
        else:
            return response

    def update_list_status(self, data):
        """
        Subscribe a contact to a list or unsubscribe a contact from a list.


        Args:
            data:

        Returns:

        """
        return self.client._post("/contactLists", json=data)

    def update(self, contact_id, data):
        """
        Update an existing contact


        Args:
            contact_id:
            data:

        Returns:

        """

        if 'contact' in data:
            contact_data = data
        else:
            contact_data = {
                'contact': data
            }

        response = self.client._put("/contacts/{}".format(contact_id), json=data)
        if 'contact' in response:
            return response['contact']
        else:
            return response

    def delete(self, contact_id):
        """
        Delete an existing contact


        Args:
            contact_id:

        Returns:

        """
        return self.client._delete("/contacts/{}".format(contact_id))

    def list_all(self, **params):
        """
        View many (or all) contacts by including their ID's or various filters.
        This is useful for searching for contacts that match certain criteria -
        such as being part of a certain list, or having a specific custom field value.


        Returns:

        """
        return self.client._get("/contacts", params=params)

    def list_all_automations_contact_is_in(self, contact_id):
        """


        Returns:

        """
        return self.client._get("/contacts/{}/contactAutomations".format(contact_id))

    def retrieve_score_value(self, contact_id):
        """


        Returns:

        """
        return self.client._get("/contacts/{}/scoreValues".format(contact_id))

    def add_to_automation(self, data):
        """


        Args:
            data:

        Returns:

        """
        return self.client._post("/contactAutomations", json=data)

    def retrieve_automation_contact_is_in(self, contact_automation_id):
        """


        Returns:

        """
        return self.client._get("/contactAutomations/{}".format(contact_automation_id))

    def remove_from_automation(self, contact_automation_id):
        """


        Returns:

        """
        return self.client._delete("/contactAutomations/{}".format(contact_automation_id))

    def list_all_automations(self):
        """


        Returns:

        """
        return self.client._get("/contactAutomations")

    def create_custom_field(self, data):
        """
        Create a new custom field


        Args:
            data:

        Returns:

        """
        if 'field' in data:
            field_data = data
        else:
            field_data = {
                'field': data
            }

        return self.client._post("/fields", json=field_data)['field']

    def retrieve_custom_field(self, field_id):
        """
        Retrieve an existing custom field


        Args:
            field_id:

        Returns:

        """
        return self.client._get("/fields/{}".format(field_id))

    def update_custom_field(self, field_id, data):
        """
        Update an existing custom field


        Args:
            field_id:
            data:

        Returns:

        """
        return self.client._put("/fields/{}".format(field_id), json=data)

    def delete_custom_field(self, field_id):
        """
        Delete an existing custom field


        Args:
            field_id:

        Returns:

        """
        return self.client._delete("/fields/{}".format(field_id))

    def list_all_custom_fields(self, **params):
        """

        Returns:

        """
        return self.client._get("/fields", params=params)

    def add_field_to_list(self, list_id, field_id):
        """

        Create a custom field relationship to list(s)

        Example:
            data = {
                "field": 8,
                "relid": 2
            }

        Args:
            data:

        Returns:

        """

        data = {
            "fieldRel": {
                "field": field_id,
                "relid": list_id
            }
        }

        response = self.client._post("/fieldRels", json=data)
        if 'fieldRel' in response:
            return response['fieldRel']
        else:
            return response

    def create_custom_field_options(self, data):
        """

        Args:
            data:

        Returns:

        """
        return self.client._post("/fieldOption/bulk", json=data)

    def create_custom_field_value(self, data):
        return self.client._post("/fieldValues", json=data)
    
    def retrieve_custom_field_value(self, field_value_id):
        return self.client._get("/fieldValues/{}".format(field_value_id))

    def update_custom_field_value_for_contact(self, data, field_value_id):
         return self.client._put("/fieldValues/{}".format(field_value_id), json=data)

    def delete_custom_field_value(self, field_value_id):
        return self.client._delete("/fieldValues/{}".format(field_value_id))

    def list_all_custom_field_values(self):
        return self.client._get("/fieldValues")
    
    def retrieve_contacts_field_values(self, contact_id):
        return self.client._get("/contacts/{}/fieldValues".format(contact_id))
    
    def retrieve_contacts_tracking_logs(self, contact_id):
        return self.client._get("/contacts/{}/trackingLogs".format(contact_id))
    
    def retrieve_contacts_data(self, contact_id):
        return self.client._get("/contacts/{}/contactData".format(contact_id))
    
    def retrieve_contacts_bounce_logs(self, contact_id):
        return self.client._get("/contacts/{}/bounceLogs".format(contact_id))
    
    def retrieve_contacts_geo_ips(self, contact_id):
        return self.client._get("/contacts/{}/geoIps".format(contact_id))
    
    def retrieve_contacts_organization(self, contact_id):
        return self.client._get("/contacts/{}/organization".format(contact_id))

    def retrieve_contacts_account_contacts(self, contact_id):
        return self.client._get("/contacts/{}/accountContacts".format(contact_id))
    
    def retrieve_contacts_automation_entry_counts(self, contact_id):
        return self.client._get("/contacts/{}/automationEntryCounts".format(contact_id))

    def add_tag_to_contact(self, data):
        """
        Add a tag to a contact

        :param data:
        :return:
        """
        return self.client._post("/contactTags", json=data)

    def remove_tag_from_a_contact(self, contact_tag_id):
        """
        Remove a tag from a contact

        :param contact_tag_id: The contact tag id
        :return:
        """
        return self.client._delete("/contactTags/{}".format(contact_tag_id))

    def retrieve_contact_tags(self, contact_id):
        """
        Retrieve all tags from a contact

        :param contact_id:
        :return:
        """
        return self.client._get("/contacts/{}/contactTags".format(contact_id))

    def retrieve_field_options(self, field_id):
        """


        Args:
            field_id:

        Returns:

        """
        return self.client._get("/fields/{}/options".format(field_id))
