from system.dog_system import Dog_System




if __name__ == "__main__":
    system = Dog_System()

    state_cmd = [0, 0, 0,
                 0, 0, 0,
                 0, 0, 0,
                 0, 0, 0]

    system.advance(state_cmd)
