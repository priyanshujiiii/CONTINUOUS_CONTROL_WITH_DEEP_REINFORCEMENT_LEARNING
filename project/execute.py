from ddpg import Agent
import gym
import numpy as np
import matplotlib.pyplot as plt


env  =  gym.make('LunarLanderContinuous-v2')
agent = Agent(alpha=0.000025,beta=0.00025, input_dims=[8], tau=0.001, env=env, batch_size=64, layer1_size=400, layer2_size=300, n_actions=2)

np.random.seed(0)

score_history = []
for i in range(3000):
    observation = env.reset()
    done = False
    score = 0
    while not done:
        action = agent.choose_action(observation)
        observation_, reward, done, info = env.step(action)
        agent.remember(observation, action, reward, observation_, done)
        agent.learn()
        observation = observation_
        score += reward
    score_history.append(score)
    print('episode ', i, 'score %.2f' % score, 'trailing 100 games %.2f' % np.mean(score_history[-100:]))
    if i % 25 == 0:
        agent.save_models()
    
filename = "project.png"

def plot_learning_curve(x, scores, filename):
    if len(scores) < 100:
        plt.plot(x, scores)
        plt.title('Score per Episode')
        plt.xlabel('Episode')
        plt.ylabel('Score')
    else:
        running_avg = np.convolve(scores, np.ones((100,))/100, mode='valid')
        plt.plot(x[-len(running_avg):], running_avg)
        plt.title('Running average of previous 100 scores')
        plt.xlabel('Episode')
        plt.ylabel('Score')
    plt.savefig(filename)
    plt.close()
plot_learning_curve(range(len(score_history)), score_history, filename)
print('Training complete. Models saved.')