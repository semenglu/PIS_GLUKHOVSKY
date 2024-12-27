
from Client_rep_base import  ClientRepBase


class ClientAdapter:
    def __init__(self, client_rep_base: ClientRepBase):
        self._client_rep_base = client_rep_base

    def get_k_n_short_list(self, n, k):
        return self._client_rep_base.get_k_n_short_list(n, k)

    def get_by_id(self, client_id):
        return self._client_rep_base.get_by_id(client_id)

    def delete_client_by_id(self, client_id):
        self._client_rep_base.delete_client_by_id(client_id)

    def update_client_by_id(self, client_id, **kwargs):
        self._client_rep_base.update_client_by_id(client_id, **kwargs)

    def add_client(self, surname, first_name, patronymic, email, phone_number, passport_number, comment):
        self._client_rep_base.add_client(surname, first_name, patronymic, email, phone_number, passport_number, comment)

    def get_count(self):
        return self._client_rep_base.get_count()

    def sort_by_field(self, field_name):
        self._client_rep_base.sort_by_field(field_name)

    def is_client_exist_by_passport(self, passport_number):
        return self._client_rep_base.is_client_exist_by_passport(passport_number)

    def convert_data(self, input_filename, output_filename, input_strategy_class, output_strategy_class):
        self._client_rep_base.convert_data(input_filename, output_filename, input_strategy_class, output_strategy_class)
