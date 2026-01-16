from cinema import CinemaSystem, Cinema

def main():
    cinema_system = CinemaSystem()
    cinema_central = Cinema("Central World", "Central World")
    cinema_system.add_cinema(cinema_central)
    cinema_system.show_cinema()
    print("Commit feature_user")

if __name__ == "__main__":
    main()