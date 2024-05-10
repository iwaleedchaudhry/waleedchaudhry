import uuid
import pickle

class SystemAdministrator:
    def __init__(self):
        self.movie_listings = {}
        self.screens = {}

    def create_movie_listing(self, title, seats):
        if title in self.movie_listings:
            print(f"Movie {title} already exists.")
            return
        self.movie_listings[title] = Movie(title, seats)
        print(f"Movie {title} created with {seats} seats.")



    def save_movie_listings(self):
        with open('movie_listings.pkl', 'wb') as f:
            pickle.dump(self.movie_listings, f)

    def load_movie_listings(self):
        try:
            with open('movie_listings.pkl', 'rb') as f:
                self.movie_listings = pickle.load(f)
        except FileNotFoundError:
            print("No movie listings file found.")


    def establish_screen(self, number):
        if number in self.screens:
            print(f"Screen {number} already exists.")
            return
        self.screens[number] = Screen(number)
        print(f"Screen {number} established.")

    def assign_movie_to_screen(self, title, number):
        if title not in self.movie_listings:
            print(f"Movie {title} does not exist.")
            return
        if number not in self.screens:
            print(f"Screen {number} does not exist.")
            return
        self.screens[number].assign_movie(self.movie_listings[title])
        print(f"Movie {title} assigned to screen {number}.")

class User:
    def __init__(self, username):
        self.username = username
        self.password_hash = None
        self.bookings = []

    def register_account(self, password):
        self.password_hash = password
        print(f"Account registered for {self.username}.")

    def select_movie(self, movie_title):
        self.selected_movie = movie_title
        print(f"Selected movie: {self.selected_movie}")

    def select_seats(self, number_of_seats):
        self.selected_seats = number_of_seats
        print(f"Selected seats: {self.selected_seats}")

    def make_reservation(self, movie, number_of_seats):
        if movie.seats >= number_of_seats:
            movie.seats -= number_of_seats
            self.bookings.append((movie.title, number_of_seats))
            print(f"Reservation made for {number_of_seats} seats for {movie.title}.")
        else:
            print("Not enough seats available.")

    @staticmethod
    def save_users(users):
        with open('users.pkl', 'wb') as f:
            pickle.dump(users, f)

    @staticmethod
    def load_users():
        try:
            with open('users.pkl', 'rb') as f:
                return pickle.load(f)
        except FileNotFoundError:
            print("No users file found.")
            return {}


    def select_movie(self, movie_title):
        print(f"{self.username} selected movie {movie_title}.")

    def select_seats(self, number_of_seats):
        print(f"{self.username} selected {number_of_seats} seats.")

    def make_reservation(self, movie, seats):
        booking = BookingDetails(self, movie, seats)
        self.bookings.append(booking)
        print(f"{self.username} made a reservation for {movie.title} with {seats} seats.")

class Movie:
    def __init__(self, title, seats):
        self.title = title
        self.seats = seats

class Screen:
    def __init__(self, number):
        self.number = number
        self.current_movie = None

    def assign_movie(self, movie):
        self.current_movie = movie
        print(f"Screen {self.number} now showing {movie.title}.")

class Timeslot:
    def __init__(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time

    def get_duration(self):
        return self.end_time - self.start_time

    def __str__(self):
        return f"{self.start_time} - {self.end_time}"


class BookingDetails:
    def __init__(self, user, movie, seats):
        self.user = user
        self.movie = movie
        self.seats = seats
        self.booking_id = uuid.uuid4()
    def generate_receipt(self):
        return f"Booking ID: {self.booking_id}\nUser: {self.user.username}\nMovie: {self.movie.title}\nSeats: {self.seats}"
    

def main():
    admin = SystemAdministrator()
    users = User.load_users()
    user = {}
    admin.load_movie_listings()


    while True:
        print("\n1. Register account")
        print("2. Log in")
        print("3. View movie listings")
        print("4. Select movie")
        print("5. Select seats")
        print("6. Make reservation")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")
            user = User(username)
            user.register_account(password)
            users[username] = user
            with open('users.pkl', 'wb') as f:
                pickle.dump(users, f)
        elif choice == '2':
            username = input("Enter username: ")
            password = input("Enter password: ")
            if user and user.username == username and user.password_hash == password:
                print("Logged in successfully.")
            else:
                print("Invalid username or password.")
        elif choice == '3':
            for title in admin.movie_listings:
                print(title)
        elif choice == '4':
            if user:
                movie_title = input("Enter movie title: ")
                user.select_movie(movie_title)
            else:
                print("You need to log in first.")
        elif choice == '5':
            if user:
                number_of_seats = int(input("Enter number of seats: "))
                user.select_seats(number_of_seats)
            else:
                print("You need to log in first.")
        elif choice == '6':
            if user:
                movie_title = input("Enter movie title: ")
                number_of_seats = int(input("Enter number of seats: "))
                movie = admin.movie_listings.get(movie_title)
                if movie and movie.seats >= number_of_seats:
                    user.make_reservation(movie, number_of_seats)
                else:
                    print("Invalid movie title or not enough seats.")
            else:
                print("You need to log in first.")
        elif choice == '7':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()