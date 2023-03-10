
DATA_DIR = './data'             # Folder for data files and images
WORD_DICT = './word_dict.json'  # Vocabulary file
IMG_SIZE = 299                  # Shape size of the encoder input images
NUM_WORKERS = 6                 # Dataloader workers count
BATCH_SIZE = 16                 # Batch size for mini-batch gradient descent
START_EPOCH = 1                 # Starting epoch for the experiment
NUM_EPOCHS = 1                  # Number of epochs for which training is to be performed
LOG_INTERVAL = 500              # Frequency for logging statistics
LR = 4e-4                       # Learning rate
STEP_SIZE = 5                   # Step size for learning rate annealing
ALPHA_C = 1                     # Regularization constant
ENCODER_DIM = 2048              # The output dimension of the encoder
TF_RATIO = 0                    # Teacher Forcing is used always
LOG_FILE = './data/log.txt'     # Creation of the log file for logging statistics
MODEL_PATH = None               # Path to pretrained model
BEAM_SIZES = [3, 6, 9]          # List of used beam size values
MAX_STEPS = 50                  # Max steps in beam search algorithm
MIN_LENGTH = 8                  # Number of first words of the caption for random reducing the score
KMAX = 4                        # Max possible length in words of possible duplicated group in caption
