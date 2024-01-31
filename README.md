# PixelPerfector

A Telegram bot that increases the resolution of the input image. The basis of this bot is a neural network model named Real-ESRGAN -- an approach to solving the Single Image Super Resolution task, based
on generative adversarial networks. Real-ESRGAN is capable of enhancing details and removing artifacts in images. The model is borrowed [from this repository](https://github.com/ai-forever/Real-ESRGAN), which is not the original implementation, and
has been slightly adapted.

- Article: [Real-ESRGAN: Training Real-World Blind Super-Resolution with Pure Synthetic Data](https://arxiv.org/abs/2107.10833)
- [Original implementation](https://github.com/xinntao/Real-ESRGAN)

### Installation

1. Clone the repository to your local machine:
    ```
    git clone https://github.com/alinakitieva/pixel-perfector
    ```

2. Navigate to the cloned directory:

    ```
    cd pixel-perfector
    ```

3. Install the required Python packages:

    ```commandline
    pip install -r requirements.txt
    ```

4. Create a .env file in the root directory of the project and add the following environment variables:

```dotenv
BOT_TOKEN=<your_bot_token>
ADMIN_IDS=<your_admin_ids>
```

### Running the Application
Start the application by running:

```commandline
python main.py
```