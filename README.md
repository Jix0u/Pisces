
# Pisces: Video Ad Generator Background Music with RNN (LSTMs)
Pisces is a video advertisement generator using Cohere (chat API), Hugging Face (video generation), Google (text to speech) and a background music generation model that harnesses the power of Recurrent Neural Networks (RNNs) specifically Long Short-Term Memory (LSTM) units. This model generates soothing background music tailored to text prompts and advertisements by learning from a vast database of MIDI files.

## How it Works
1. **User Input**: The user provides a text prompt describing the desired advertisement. This could include product details, target audience, desired tone, and other relevant information.
2. **Cohere Chat API**: The text prompt is processed using Cohere's chat API, which generates a coherent and engaging ad script based on the provided input.
3. **Video Generation**: The generated ad script is then fed into Hugging Face's video generation model. This model creates a visual representation of the script, producing a video that aligns with the described advertisement.
4. **Voice Over**: Google’s text-to-speech API is used to convert the ad script into natural-sounding speech. This voiceover is synchronized with the video to provide an engaging auditory experience.
5. **Background Music Generation RNNs (LSTMs)**: The background music generation model is trained on a vast database of MIDI files. It utilizes Recurrent Neural Networks (RNNs), specifically Long Short-Term Memory (LSTM) units, which are effective in capturing temporal dependencies in music sequences. Given the ad script, the model generates soothing background music that complements the tone and mood of the advertisement. The LSTM units ensure the music flows naturally and fits well with the video's narrative.
6. **Final Output**: The generated video, synchronized voiceover, and background music are integrated to produce the final advertisement. The result is a cohesive video ad with engaging visuals, clear narration, and soothing background music tailored to the content.

## Sample Generated Video from Text Prompts
https://github.com/Jix0u/Pisces/assets/55889031/546749d5-d6c8-4b11-925c-b76d0376dbdb

## Sample Generated Music from Text Prompts
https://github.com/Jix0u/AudioGenesis/assets/55889031/490030bb-aba8-4ee6-9a1d-496fdea8b94e

https://github.com/Jix0u/AudioGenesis/assets/55889031/2983c477-ffb3-4cbf-96be-d774bf29efc4

## References
The architecture of Pisces draws inspiration from the advancements in LSTM-based music generation models.

## Usage
To utilize Pisces and generate background music from text prompts, follow these steps:

### Notebook Contents
Inside the repository, you will find:

- **Model Definition**: Details regarding the architecture of Audiogenesis, including LSTM units and text prompt embedding techniques.
- **Training Scripts**: Scripts and code for training the Audiogenesis model using your own MIDI dataset or pre-existing data.
- **Inference Code**: Code for generating background music using the trained model. You can input your text prompts to receive musical compositions.
- **Evaluation Techniques**: Techniques for evaluating the quality of generated music, ensuring coherence and relevance to the given text prompts.

The repository includes MIDI files alongside corresponding text prompts for training and evaluation purposes.

