from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch
from custom_logging.custom_logger import Customlogger
from utils.config_loader import ConfigLoader


device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

class TextSummarization:
    def __init__(self, documents = None):
        self.logger = Customlogger.create_custom_logger("TextSummarization")
        try:
            self.config = ConfigLoader.load_config(file_name = "config.yaml")
            if self.config is None:
                raise ValueError("Failed to load configuration for model name.")
                
            self.documents = documents
            self.model_summary_name = self.config.get("name_summary_model")
            self.tokenizer = None
            self.model_summary = None
            self.min_length = self.config.get("min_length")
            self.max_length = self.config.get("max_length")
            self.num_beams = self.config.get("num_beams")
        except Exception as e:
            self.logger.error(f"Error initializing TextSummarization: {e}")
            raise

    def load_models(self):
        try:
            self.logger.info(f"Loading model: {self.model_summary_name}")
            self.tokenizer = AutoTokenizer.from_pretrained(self.model_summary_name)
            self.model_summary = AutoModelForSeq2SeqLM.from_pretrained(self.model_summary_name)
            self.model_summary = self.model_summary.to(device)

            if not self.tokenizer or not self.model_summary:
                raise ValueError("Model or Tokenizer is not initialized properly.")

            self.logger.info("Model loaded successfully.")
        except Exception as e:
            self.logger.error(f"Failed to load model: {e}")
            self.tokenizer = None
            self.model_summary = None
            raise



    def build_summarize_model(self, document):
        try:
            if not self.tokenizer or not self.model_summary:
                raise ValueError("Model or Tokenizer is not initialized.")

            input = self.tokenizer(
                document, 
                return_tensors = "pt", 
                truncation=True, 
                padding=True
            ).to(device)
            summary_process = self.model_summary.generate(
                input["input_ids"],
                min_length = self.min_length,
                max_length = self.max_length,
                num_beams = self.num_beams,
                early_stopping = True
            )
            output = self.tokenizer.decode(
                summary_process[0], 
                skip_special_tokens = True
            )
            return output
        except Exception as e:
            self.logger.error(f"Error summarizing text: {e}")
            raise


    
    def summarize_document(self, chunks):
        try:
            logger = Customlogger.create_custom_logger("summarizationDocument")
            logger.info("Starting document summarization.")
            summary = []

            # Summarize each chunk
            for chunk in chunks:
                try:
                    chunk_summary = self.build_summarize_model(chunk)  # Access chunk content correctly
                    if chunk_summary:
                        summary.append(chunk_summary)
                except Exception as e:
                    logger.error(f"Error summarizing chunk {e}")

            # Concatenate all summaries
            logger.info("Concatenating summaries for final summarization.")
            summarize_text = " ".join(summary)
            
            logger.info("Document summarization completed successfully.")
            return summarize_text

        except Exception as e:
            logger.error(f"Error during document summarization: {e}")
            raise