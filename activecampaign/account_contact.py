class AccountContact(object):
    def __init__(self, client):
        self.client = client

    def create_association(self, account_id, contact_id):
        """
        Create a new association


        Args:
            data:

        Returns:

        """

        data = {
            "accountContact": {
                "contact": contact_id,
                "account": account_id,
            }
        }
        response = self.client._post(f"/accountContacts", json=data)
        if 'accountContact' in response:
            return response['accountContact']
        else:
            return response

    def update_association(self, association_id, account_id, contact_id):
        """
        Update an association


        Args:
            association_id:
            account_id:
            contact_id:

        Returns:

        """
        data = {
            "accountContact": {
                "contact": contact_id,
                "account": account_id,
            }
        }
        return self.client._put(f"/accountContacts/{association_id}", json=data)

    def retrieve_association(self, association_id):
        """
        Retrieve an existing association


        Args:
            contact_id:

        Returns:

        """
        return self.client._get(f"/accountContacts/{association_id}")

    def delete_association(self, association_id):
        """
        Delete an existing association


        Args:
            account_id:

        Returns:

        """
        return self.client._delete(f"/accountContacts/{association_id}")

    def list_all_associations(self, **params):
        """
        View many (or all) association by including their ID's or various filters.
        This is useful for searching for accounts that match certain criteria -
        such as having a specific custom field value.


        Returns:

        """
        return self.client._get("/accountContacts", params=params)
