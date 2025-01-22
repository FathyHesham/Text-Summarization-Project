# Import Libraries
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from utils.config_loader import ConfigLoader
from custom_logging.custom_logger import Customlogger

# Load configuration from config.yaml file
config = ConfigLoader.load_config(file_name="config.yaml")
# Create a custom logger instance for this module
logger = Customlogger.create_custom_logger("Load_And_Chunk_Document")

# Function to load PDF documents
def load_documents(file_path):
    try:
        # Create a PDF loader instance with the given file path
        loader = PyPDFLoader(file_path)
        # Load the document using the loader
        document = loader.load()
        # Log successful document loading
        logger.info("Document loaded successfully.")
        # Return the loaded document
        return document
    except Exception as e:
        # Log any errors during document loading
        logger.error(f"Error loading document from {file_path}: {e}")
        # Re-raise the exception
        raise

# Function to split document into smaller chunks
def chunk_document(document):
    try:
        # Create a text splitter with configured chunk size and overlap
        chunk_text = RecursiveCharacterTextSplitter(
            chunk_size = config.get("chunk_size"),      # Set the size of each chunk
            chunk_overlap = config.get("chunk_overlap"), # Set the overlap between chunks
        )
        # Split the document into chunks
        chunks = chunk_text.split_text(document)
        # Log successful chunking operation
        logger.info(f"Document chunked successfully into {len(chunks)} chunks.")
        # Return the chunks
        return chunks
    except Exception as e:
        # Log any errors during chunking
        logger.error(f"Error chunking the document: {e}")
        # Re-raise the exception
        raise
