from telebot.handler_backends import State, StatesGroup


class UserInputState(StatesGroup):
    command = State()
    input_city = State()
    destinationId = State()
    photo_need = State()
    photo_count = State()
    pageSize = State()
    checkIn = State()
    checkOut = State()
    priceMin = State()
    priceMax = State()
    sortOrder = State()
    landmark_lds_In = State()
    landmark_lds_Out = State()
