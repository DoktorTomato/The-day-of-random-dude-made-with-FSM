'''
This script has a FSM of my day and all the dunctions helping to implement it
'''
import random

def prime(fn):
    def wrapper(*args, **kwargs):
        v = fn(*args, **kwargs)
        v.send(None)
        return v
    return wrapper

def day():
    '''
    This is the generator that returns a current hour
    '''
    hour = 0
    while True:
        if hour >= 24:
            break
        yield hour
        hour += 1

class MyDay:
    '''
    This class is a FSM that imitates my day
    '''
    def __init__(self) -> None:
        '''
        This method initializes object of this class
        '''
        self.sleeping_state = self._create_sleeping_state()
        self.randomly_awake_state = self._create_randomly_awake_state()
        self.awake_state = self._create_awake_state()
        self.lately_awake_stete = self._create_lately_awake_stete()
        self.eating_state = self._create_eating_state()
        self.studying_state = self._create_studying_state()
        self.idle_state = self._create_idle_state()
        self.toilet_state = self._create_toilet_state()
        self.suicidal_state = self._create_suicidal_state()
        self.resting_state = self._create_resting_state()

        self.clock = day()

        self.current_state = self.sleeping_state

    def send(self, sent_action):
        '''
        This method sends an action to current state
        '''
        self.current_state.send(sent_action)

    @prime
    def _create_sleeping_state(self):
        '''
        This method creates a sleeping state
        '''
        while True:
            action = yield
            cur_hour = next(self.clock)
            insomnia_factor = random.randrange(0, 5)

            if cur_hour == 23:
                print('It\'s the end of the day. Goodnight')
            elif insomnia_factor == 1:
                self.current_state = self.randomly_awake_state
                print('Huh? Why am I awake?')
            elif action == 'Awake' and cur_hour < 7:
                self.current_state = self.sleeping_state
                print('Please no, 5 more minutes')
            elif action == 'Awake' and 7 <= cur_hour < 12:
                self.current_state = self.awake_state
                print('WAKEY, WAKEY IT\'S TIME FOR SCHOOL')
            elif action == 'Awake' and cur_hour >= 12:
                self.current_state = self.lately_awake_stete
                print('Ugh... what time it is? I\'m late for everything')
            else:
                self.current_state = self.sleeping_state
                print('I can\'t I\'m sleeping now')

    @prime
    def _create_randomly_awake_state(self):
        '''
        This method creates a randomly awake state of machine
        '''
        while True:
            action = yield
            cur_hour = next(self.clock)
            self.current_state = self.sleeping_state
            print('I\'ll try to sleep again...')
            self.current_state.send(action)

    @prime
    def _create_awake_state(self):
        '''
        This method creates an awake state of machine
        '''
        while True:
            action = yield
            cur_hour = next(self.clock)

            if action == 'Study':
                self.current_state = self.studying_state
                print('It\'s time to work')
            elif action == 'Eat':
                self.current_state = self.eating_state
                print('It\'s time to eat')
            elif (action == 'read' or
                  action == 'watch videos' or
                  action == 'play games' or
                  action == 'walk'):
                self.current_state = self.resting_state
                print(f'It\'s time to {action}')
            else:
                raise ValueError(f'Unkown action:{action}')

    @prime
    def _create_lately_awake_stete(self):
        '''
        This method creates an lately awake state of machine
        '''
        while True:
            action = yield
            cur_hour = next(self.clock)

            if action == 'Study':
                self.current_state = self.studying_state
                print('No time! I need to study')
            elif (action == 'read' or
                  action == 'watch videos' or
                  action == 'play games' or
                  action == 'walk'):
                self.current_state = self.resting_state
                print(f'I missed everything anyway might as well {action}')
            else:
                raise ValueError(f'Unkown action:{action}')

    @prime
    def _create_eating_state(self):
        '''
        This method creates an eating state of machine
        '''
        while True:
            action = yield
            cur_hour = next(self.clock)
            if action == 'Study':
                self.current_state = self.studying_state
                print('Time to work')
            else:
                self.current_state = self.idle_state
                print('What shall I do next?')

    @prime
    def _create_studying_state(self):
        '''
        This method creates a studying state of machine
        '''
        while True:
            action = yield
            cur_hour = next(self.clock)
            toilet_factor = random.randrange(0, 5)
            suicidal_factor = random.randrange(0, 5)

            if cur_hour >= 17:
                self.current_state = self.idle_state
                print('I\'m tired now')
            elif toilet_factor == 1:
                self.current_state = self.toilet_state
                print('Upsie. I neeed to go to the toilet')
            elif suicidal_factor == 1:
                self.current_state = self.suicidal_state
                print("I'm so disappointed in myself")
            elif action == 'Eat':
                self.current_state = self.eating_state
                print('Time to consume food')
            elif action == 'Study':
                self.current_state = self.studying_state
            else:
                raise ValueError(f'Unkown action:{action}')

    @prime
    def _create_idle_state(self):
        '''
        This method that create an idle sate of machine
        '''
        while True:
            action = yield
            cur_hour = next(self.clock)
            toilet_factor = random.randrange(0, 5)
            suicidal_factor = random.randrange(0, 5)

            if toilet_factor == 1:
                self.current_state = self.toilet_state
                print('Upsie. I neeed to go to the toilet')
            elif suicidal_factor == 1:
                self.current_state = self.suicidal_state
                print("I'm so disappointed in myself")
            if action == 'Study':
                self.current_state = self.studying_state
                print('I need to study')
            elif action == 'Eat':
                self.current_state = self.eating_state
                print('Time to consume food')
            elif (action == 'read' or
                action == 'watch videos' or
                action == 'play games' or
                action == 'walk'):
                self.current_state = self.resting_state
                print(f'It\'s time to {action}')
            elif action == 'Sleep' and cur_hour >= 22:
                self.current_state = self.sleeping_state
                print('Time to sleep')
            else:
                raise ValueError(f'Unkown action:{action}')

    @prime
    def _create_toilet_state(self):
        '''
        This method that create an toilet sate of machine
        '''
        while True:
            action = yield
            cur_hour = next(self.clock)
            self.current_state = self.idle_state
            print('What shall i do next?')
            self.current_state.send(action)

    @prime
    def _create_suicidal_state(self):
        '''
        This method that create an suicidal sate of machine
        '''
        while True:
            action = yield
            cur_hour = next(self.clock)
            self.current_state = self.idle_state
            print('I\'m not suicidal now. What shall i do next?')
            self.current_state.send(action)

    @prime
    def _create_resting_state(self):
        '''
        This method that create an resting sate of machine
        '''
        while True:
            action = yield
            cur_hour = next(self.clock)

            if action == 'Study':
                self.current_state = self.studying_state
                print('I need to study')
            elif action == 'Eat':
                self.current_state = self.eating_state
                print('Time to consume food')
            elif (action == 'read' or
                action == 'watch videos' or
                action == 'play games' or
                action == 'walk'):
                self.current_state = self.resting_state
                print(f'It\'s time to {action}')
            elif action == 'Sleep' and cur_hour >= 22:
                self.current_state = self.sleeping_state
                print('Time to sleep')
            else:
                raise ValueError(f'Unkown action:{action}')

    def run_the_day(self, list_of_actions):
        '''
        This function runs a day machine
        '''
        try:
            for action in list_of_actions:
                self.send(action)
        except RuntimeError:
            print('The day has ended!')

if __name__ == '__main__':
    ivan_shevchuk = MyDay()
    action_list = ['read', 'read', 'read', 'Eat', 'walk',
                   'Study', 'read', 'Awake', 'Eat', 'Study',
                   'Study', 'Study', 'Study', 'Eat', 'read',
                   'play games', 'watch videos', 'watch videos',
                   'read', 'Sleep']
    ivan_shevchuk.run_the_day(action_list)
