class Accounts(object):
    def __init__(self, client):
        self.client = client

    def create(self, data):
        """
        Create a new account

        Example:
            data = {
                "name": "Example Account",
                "accountUrl": "https://www.example.com",
                "owner": 1,
                "fields": [
                    {
                        "customFieldId": 9,
                        "fieldValue": "500-1000"
                    },
                    {
                        "customFieldId": 20,
                        "fieldValue": 1234,
                        "fieldCurrency": "GBP"
                    }
                ]
            }

        Args:
            data:

        Returns:

        """

        if 'account' in data:
            account_data = data
        else:
            account_data = {
                'account': data
            }

        response = self.client._post("/accounts", json=account_data)
        if 'account' in response:
            return response['account']
        else:
            return response

    def update(self, account_id, data):
        """
        Update an account

        Example:
            data = {
                "name": "Example Account",
                "accountUrl": "https://www.example.com",
                "owner": 1,
                "fields": [
                    {
                        "customFieldId": 9,
                        "fieldValue": "500-1000"
                    },
                    {
                        "customFieldId": 20,
                        "fieldValue": 1234,
                        "fieldCurrency": "GBP"
                    }
                ]
            }

        Args:
            account_id:
            data:

        Returns:

        """

        if 'account' in data:
            account_data = data
        else:
            account_data = {
                'account': data
            }

        response = self.client._put(f"/accounts/{account_id}", json=account_data)
        if 'account' in response:
            return response['account']
        else:
            return response

    def retrieve(self, account_id):
        """
        Retrieve an existing contact


        Args:
            contact_id:

        Returns:

        """
        return self.client._get("/accounts/{}".format(account_id))

    def delete(self, account_id):
        """
        Delete an existing account


        Args:
            account_id:

        Returns:

        """
        return self.client._delete("/accounts/{}".format(account_id))

    def list_all(self, **params):
        """
        View many (or all) accounts by including their ID's or various filters.
        This is useful for searching for accounts that match certain criteria -
        such as having a specific custom field value.


        Returns:

        """
        return self.client._get("/accounts", params=params)

    def create_custom_field(self, data):
        """
        Create a new custom field


        Args:
            data:

        Returns:

        """

        if 'accountCustomFieldMetum' in data:
            field_data = data
        else:
            field_data = {
                'accountCustomFieldMetum': data
            }

        response = self.client._post("/accountCustomFieldMeta", json=field_data)
        if 'accountCustomFieldMetum' in response:
            self.add_custom_field_to_group(response['accountCustomFieldMetum']['id'])
            return response['accountCustomFieldMetum']
        else:
            return response

    def add_custom_field_to_group(self, field_id, group_id=3, ordernum=None):
        """
        Add Custom Field to Field Group

        :param field_id:
        :param group_id:
        :param ordernum:
        :return:
        """
        payload = {
            "groupMember": {
                "rel_id": str(field_id),
                "ordernum": ordernum,
                "group_id": str(group_id)
            }
        }

        return self.client._post("/groupMembers", json=payload)

    def update_custom_field_group(self, field_id, group_id=3, ordernum=None):
        """
        Update Custom Field Group

        :param field_id:
        :param group_id:
        :param ordernum:
        :return:
        """
        payload = {
            "groupMember": {
                "rel_id": str(field_id),
                "ordernum": ordernum,
                "group_id": str(group_id)
            }
        }

        return self.client._put(f"/groupMembers/{group_id}", json=payload)

    def retrieve_custom_field(self, field_id):
        """
        Retrieve an existing custom field


        Args:
            field_id:

        Returns:

        """
        return self.client._get("/accountCustomFieldMeta/{}".format(field_id))

    def update_custom_field(self, field_id, data):
        """
        Update an existing custom field


        Args:
            field_id:
            data:

        Returns:

        """
        return self.client._put("/accountCustomFieldMeta/{}".format(field_id), json=data)

    def delete_custom_field(self, field_id):
        """
        Delete an existing custom field


        Args:
            field_id:

        Returns:

        """
        return self.client._delete("/accountCustomFieldMeta/{}".format(field_id))

    def list_all_custom_fields(self, **params):
        """

        Returns:

        """
        return self.client._get("/accountCustomFieldMeta", params=params)

    # def create_a_custom_field_relationship_to_list(self, data):
    #     """
    #
    #     Args:
    #         data:
    #
    #     Returns:
    #
    #     """
    #     return self.client._post("/fieldRels", json=data)
    #
    # def create_custom_field_options(self, data):
    #     """
    #
    #     Args:
    #         data:
    #
    #     Returns:
    #
    #     """
    #     return self.client._post("/fieldOption/bulk", json=data)

    def create_custom_field_value(self, data):
        return self.client._post("/accountCustomFieldData", json=data)

    def retrieve_custom_field_value(self, field_value_id):
        return self.client._get("/accountCustomFieldData/{}".format(field_value_id))

    def update_custom_field_value(self, data, field_value_id):
        return self.client._put("/accountCustomFieldData/{}".format(field_value_id), json=data)

    def delete_custom_field_value(self, field_value_id):
        return self.client._delete("/accountCustomFieldData/{}".format(field_value_id))

    def list_all_custom_field_values(self):
        return self.client._get("/accountCustomFieldData")

    def retrieve_accounts_field_values(self, contact_id):
        return self.client._get("/accountCustomFieldMeta/{}/accountCustomFieldData".format(contact_id))
