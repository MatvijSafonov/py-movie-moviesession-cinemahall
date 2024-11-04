from db.models import CinemaHall


def get_cinema_halls() -> None:
    return CinemaHall.objects.all()


def create_cinema_hall(
        hall_name: None,
        hall_rows: None,
        hall_seats_in_row: None
) -> None:
    return CinemaHall.objects.create(
        name=hall_name,
        rows=hall_rows,
        seats_in_row=hall_seats_in_row
    )
