from django.db import models

# PART 1.1

class Customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

class Order(models.Model):
    order_number = models.IntegerField()
    order_time = models.DateTimeField()
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')

# PART 1.2

class Breed(models.Model):
    breed_type = models.CharField(max_length=255)

class Owner(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    number = models.IntegerField()

class Pet(models.Model):
    name = models.CharField(max_length=255)
    breed_id = models.ForeignKey(Breed, on_delete=models.CASCADE, related_name='pets')
    ownder_id = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='pets')

class Clinic(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    number = models.IntegerField()

class Vet(models.Model):
    name = models.CharField(max_length=255)
    clinic_id = models.ForeignKey(Clinic, on_delete=models.CASCADE, related_name='vets')

class Appointments(models.Model):
    date = models.DateTimeField()
    vet_id = models.ForeignKey(Vet, on_delete=models.CASCADE, related_name='appointments')
    pet_id = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='appointments')

# PART 1.3

class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    number = models.IntegerField()

class Chef(models.Model):
    name = models.CharField(max_length=255)
    restaurant_id = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='chefs')

class Publication(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    number = models.IntegerField()

class Critic(models.Model):
    name = models.CharField(max_length=255)
    publication_id = models.ForeignKey(Publication, on_delete=models.CASCADE, related_name='critics')

class Review(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateTimeField()
    restaurant_id = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='reviews')
    critic_id = models.ForeignKey(Critic, on_delete=models.CASCADE, related_name='reviews')

# PART 2.1

class Film(models.Model):
    title = models.CharField(max_length=255)
    release_date = models.DateTimeField()

class Viewer(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()

class Film_Viewer(models.Model):
    film_id = models.ForeignKey(Film, on_delete=models.CASCADE, related_name='film_viewers')
    viewer_id = models.ForeignKey(Viewer, on_delete=models.CASCADE, related_name='film_viewers')

# PART 2.2

class Worker(models.Model):
    name = models.CharField(max_length=255)
    wage = models.IntegerField()

class Shift(models.Model):
    date_time_start = models.DateTimeField()
    date_time_end = models.DateTimeField()

class Worker_Shift(models.Model):
    worker_id = models.ForeignKey(Worker, on_delete=models.CASCADE, related_name='worker_shifts')
    shift_id = models.ForeignKey(Shift, on_delete=models.CASCADE, related_name='worker_shifts')

# Part 2.3

class Book(models.Model):
    title = models.CharField(max_length=255)
    date_published = models.DateTimeField()
    genre = models.CharField(max_length=255)

class Author(models.Model):
    name = models.CharField(max_length=255)

class Reader(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()

class Chapter(models.Model):
    title = models.CharField(max_length=255)
    chapter_number = models.IntegerField()
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='chapters')

class Book_Reader(models.Model):
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='book_readers')
    reader_id = models.ForeignKey(Reader, on_delete=models.CASCADE, related_name='book_readers')

class Book_Author(models.Model):
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='book_authors')
    author_id = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='book_authors')
