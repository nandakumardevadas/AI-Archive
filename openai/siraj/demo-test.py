import gym
import universe
import random

def main():
	env = gym.make('flashgames.DuskDrive-v0')
	env.configure(remotes=1) # automatically creates a local docker container
	observation_n = env.reset()

	#Turn Variables 
	left=[('KeyEvent', 'ArrowUp', True), ('KeyEvent', 'ArrowLeft', True), ('KeyEvent', 'ArrowRight', False)]
	right=[('KeyEvent', 'ArrowUp', True), ('KeyEvent', 'ArrowLeft', False), ('KeyEvent', 'ArrowRight', True)]
	up=[('KeyEvent', 'ArrowUp', True), ('KeyEvent', 'ArrowLeft', False), ('KeyEvent', 'ArrowRight', False)]

	while True:
		event = random.choice([left, right, up])
		action_n = [event for ob in observation_n]
		observation_n, reward_n, done_n, info = env.step(action_n)
		env.render()

if __name__ == '__main__':
	main()	


