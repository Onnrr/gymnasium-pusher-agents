import torch
import torch.nn as nn
import torch.optim as optim
import gymnasium as gym
import numpy as np

# Define a simple neural network model
class PusherModel(nn.Module):
    def __init__(self, input_dim, output_dim):
        super(PusherModel, self).__init__()
        self.fc1 = nn.Linear(input_dim, 64)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(64, 64)
        self.fc3 = nn.Linear(64, output_dim)

    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        x = self.relu(x)
        x = self.fc3(x)
        return x

# Function to load the saved model and use it for predictions
def load_and_use_pusher_model(env, model_path='models\sac.cleanrl_model'):
    input_dim = env.observation_space.shape[0]
    output_dim = env.action_space.shape[0]

    # Create an instance of the model
    model = PusherModel(input_dim, output_dim)

    # Load the saved model weights
    model.load_state_dict(torch.load(model_path))

    # Set the model to evaluation mode
    model.eval()

    # Use the model for predictions
    state = env.reset()
    state = torch.from_numpy(state).float().unsqueeze(0)

    while True:
        # Replace this line with the actual prediction logic using the loaded model
        with torch.no_grad():
            action = model(state).numpy()

        next_state, reward, done, _ = env.step(action.flatten())
        next_state = torch.from_numpy(next_state).float().unsqueeze(0)

        state = next_state

        if done:
            break

# Example usage for MuJoCo Pusher environment
env = gym.make('Pusher-v4')

# Load the saved model and use it for predictions
load_and_use_pusher_model(env)