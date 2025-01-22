from langchain_ollama import OllamaLLM
from langchain.prompts import PromptTemplate
from langchain.schema.runnable import RunnableSequence
from custom_logging.custom_logger import Customlogger
from utils.config_loader import ConfigLoader
import time

class GenerateSummary:
    def __init__(self, documents):
        try:
            self.logger = Customlogger.create_custom_logger("GenerateSummary")
            self.config = ConfigLoader.load_config(file_name="config.yaml")
            if self.config is None:
                raise ValueError("Failed to load configuration for model name.")
            
            self.documents = documents
            self.llm_model = OllamaLLM(
                model=self.config.get("name_generate_model"), 
                temperature=self.config.get("temperature"), 
                streaming=True
            )

            self.prompt_template = PromptTemplate(
                input_variables=["topic", "document", "word_limit"],
                template=(
                    "Hello, could you please rephrase the following text about '{topic}' for better clarity and quality? "
                    "Focus on the main points, use proper grammar and spelling, and ensure the language is clear and concise. "
                    "Highlight all essential aspects. Please rewrite the following text in a professional and elegant manner. "
                    "Present the content in a clear and structured format. Begin with an engaging opening sentence that provides context "
                    "to the topic '{topic}'. Follow it with a logically ordered presentation of the main points. Use precise and scientific "
                    "language, incorporating essential terms where appropriate. Conclude with a brief and impactful closing sentence. "
                    "Ensure the final text appears polished and visually appealing, suitable for a professional audience. "
                    "Please limit the response to exactly {word_limit} words. The text is as follows:\n\n{document}"
                )
            )
            self.runnable_sequence = RunnableSequence(self.prompt_template | self.llm_model)
            self.logger.info("GenerateSummary class initialized successfully.")
        except Exception as e:
            self.logger.error(f"Error initializing GenerateSummary class: {e}")
            raise

    def interact(self, topic = None, word_limit = 100):
        try:
            self.topic = topic 
            self.word_limit = word_limit 
            inputs = {
                "document": self.documents,
                "topic": topic,
                "word_limit": word_limit
            }
            response = self.runnable_sequence.invoke(inputs)

            print("AI Summary : ", end="", flush=True)

            for chunk in response:
                print(chunk, end="", flush=True)
                time.sleep(0.05)

            self.logger.info("Summary generation completed.")
        except Exception as e:
            self.logger.error(f"Error in interaction: {e}")
            raise