from src.infrastructure.AnalysisQueryProcessor import AnalysisQueryProcessor


class Main:
    def __init__(self, analysis_query_processor: AnalysisQueryProcessor = AnalysisQueryProcessor()):
        self.analysis_query_processor = analysis_query_processor

    def main(self):
        while True:
            self.analysis_query_processor.run()


if __name__ == '__main__':
    Main().main()
