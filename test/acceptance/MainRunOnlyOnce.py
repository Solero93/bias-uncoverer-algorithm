from src.infrastructure.main import Main


class MainRunOnlyOnce(Main):
    def main(self):
        self.analysis_query_processor.run()
