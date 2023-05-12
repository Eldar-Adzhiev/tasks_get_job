from faker import Faker


class RandomData(Faker):

    def get_random_fullname(self):
        return self.name()

    def get_random_mail(self):
        return self.email()

    def get_random_address(self):
        return self.street_address()
