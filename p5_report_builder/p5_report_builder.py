# builder method
class Report:
    def __init__(self):
        self.title = None
        self.has_toc = False
        self.has_data = False
        self.has_chart = False
        self.has_appendix = False
    def __str__(self):
        return (
            f"Report title: {self.title}, "
            f"has toc: {self.has_toc}, "
            f"has data: {self.has_data}, "
            f"has chart: {self.has_chart}, "
            f"has appendix: {self.has_appendix}"
        )


class ReportBuilder:
    def __init__(self):
        self.report = Report()
    def add_title(self, title):
        self.report.title = title
        return self
    def add_has_toc(self, has_toc):
        self.report.has_toc = has_toc
        return self
    def add_has_data(self, has_data):
        self.report.has_data = has_data
        return self
    def add_has_chart(self, has_chart):
        self.report.has_chart = has_chart
        return self
    def add_has_appendix(self, has_appendix):
        self.report.has_appendix = has_appendix
        return self
    def build(self):
        return self.report


def main():
    #report = Report("Monthly Report", True, True, False, False)
    report = (
        ReportBuilder()
        .add_title("Monthly Report")
        .add_has_toc(True)
        .add_has_data(True)
        .add_has_chart(False)
        .add_has_appendix(False)
        .build()
    )
    print(report)

    report2 = (
        ReportBuilder()
        .add_title("Monthly Report")
        .add_has_toc(True)
        .add_has_appendix(False)
        .build()
    )
    print(report2)
main()