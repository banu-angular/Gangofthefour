# Visualize a Data Mining Tool that analyzes different file types (PDF, CSV, Doc). The high-level process is always the same: Open File, Extract Raw Data, Analyze, and Close File. The "Template" defines this fixed sequence, but allows subclasses to provide their own specific implementation for the Extract step depending on the file format.
from abc import ABC, abstractmethod
class DataMiningTool(ABC):
    def process_file(self, file_path):
        self.open_file(file_path)
        raw_data = self.extract_data(file_path)
        self.analyze_data(raw_data)
        self.close_file(file_path)

    def open_file(self, file_path):
        print(f"Opening file: {file_path}")

    @abstractmethod
    def extract_data(self, file_path):
        pass

    def analyze_data(self, raw_data):
        print(f"Analyzing data: {raw_data}")

    def close_file(self, file_path):
        print(f"Closing file: {file_path}")
class PDFDataMiningTool(DataMiningTool):
    def extract_data(self, file_path):
        print(f"Extracting data from PDF file: {file_path}")
        return "Raw data from PDF"
class CSVDataMiningTool(DataMiningTool):
    def extract_data(self, file_path):
        print(f"Extracting data from CSV file: {file_path}")
        return "Raw data from CSV"
class DocDataMiningTool(DataMiningTool):
    def extract_data(self, file_path):
        print(f"Extracting data from Doc file: {file_path}")
        return "Raw data from Doc"
# Example usage
pdf_tool = PDFDataMiningTool()
pdf_tool.process_file("data.pdf")
csv_tool = CSVDataMiningTool()
csv_tool.process_file("data.csv")
doc_tool = DocDataMiningTool()
doc_tool.process_file("data.doc")




