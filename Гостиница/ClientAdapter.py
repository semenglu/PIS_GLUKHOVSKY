from ClientRepBase import  ClientRepBase


class ClientAdapter:

    def __init__(self, client_rep_base: ClientRepBase):
        self._client_rep_base = client_rep_base

    def get_k_n_short_list(self, k, n):
        return self._client_rep_base.get_k_n_short_list(k, n)

    def get_by_id(self, client_id):
        return self._client_rep_base.get_by_id(client_id)

    def delete_by_id(self, client_id):
        self._client_rep_base.delete_by_id(client_id)
        
    def update_by_id(self, client_id, updates: dict):
        self._client_rep_base.replace_by_id(client_id, updates)

    def add(self, client: dict):
        self._client_rep_base.add_client(client)

    def get_count(self):
        return self._client_rep_base.get_count()