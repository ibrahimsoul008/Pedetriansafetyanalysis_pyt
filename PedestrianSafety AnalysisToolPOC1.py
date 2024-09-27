class SafetyReport:
    def __init__(self):
        self.reports = {}
        self.next_id = 1
    def create_report(self, report_data):
        report_id = self.next_id
        self.reports[report_id] = report_data
        self.next_id += 1
        return report_id

    def read_report(self, report_id):
        return self.reports.get(report_id, "Report not found.")

    def update_report(self, report_id, updated_data):
        if report_id in self.reports:
            self.reports[report_id] = updated_data
            return "Report updated."
        return "Report not found."

    def delete_report(self, report_id):
        if report_id in self.reports:
            del self.reports[report_id]
            return "Report deleted."
        return "Report not found."
class SafetyAnalysisManager:
    def __init__(self):
        self.analyses = {}
        self.improvements = {}
        self.next_analysis_id = 1
        self.next_improvement_id = 1
    def conduct_pedestrian_safety_analysis(self, report_id, report_data):
        analysis_id = self.next_analysis_id
        # Here we would conduct some analysis based on the report_data
        self.analyses[analysis_id] = {
            "report_id": report_id,
            "findings": f"Analysis conducted for report {report_id}: {report_data}"
        }
        self.next_analysis_id += 1
        return analysis_id

    def recommend_safety_improvements(self, analysis_id, recommendation):
        improvement_id = self.next_improvement_id
        if analysis_id in self.analyses:
            self.improvements[improvement_id] = {
                "analysis_id": analysis_id,
                "recommendation": recommendation
            }
            self.next_improvement_id += 1
            return improvement_id
        return "Analysis ID not found."
# Example usage
if __name__ == "__main__":
    # Create a Safety Report
    report_manager = SafetyReport()
    report_id = report_manager.create_report({"location": "Main St", "issues": "High traffic"})
    print(report_manager.read_report(report_id))

    # Conduct an Analysis
    analysis_manager = SafetyAnalysisManager()
    analysis_id = analysis_manager.conduct_pedestrian_safety_analysis(report_id, "High traffic in pedestrian zone.")
    print(analysis_manager.analyses)

    # Recommend Improvements
    improvement_id = analysis_manager.recommend_safety_improvements(analysis_id, "Install speed bumps and more signage.")
    print(analysis_manager.improvements)
    import unittest
class TestPedestrianSafetyAnalysisTool(unittest.TestCase):
    def setUp(self):
        self.report_manager = SafetyReport()
        self.analysis_manager = SafetyAnalysisManager()
    def test_crud_operations(self):
        # Create a report
        report_id = self.report_manager.create_report({"location": "Main St", "issues": "High traffic"})
        self.assertEqual(self.report_manager.read_report(report_id), {"location": "Main St", "issues": "High traffic"})
        # Update the report
        self.report_manager.update_report(report_id, {"location": "Main St", "issues": "Heavy congestion"})
        self.assertEqual(self.report_manager.read_report(report_id), {"location": "Main St", "issues": "Heavy congestion"})

        # Delete the report
        self.report_manager.delete_report(report_id)
        self.assertEqual(self.report_manager.read_report(report_id), "Report not found.")

    def test_safety_analysis_and_recommendations(self):
        report_id = self.report_manager.create_report({"location": "Main St", "issues": "High traffic"})
        analysis_id = self.analysis_manager.conduct_pedestrian_safety_analysis(report_id, "High traffic in pedestrian zone.")
        self.assertIn(analysis_id, self.analysis_manager.analyses)

        improvement_id = self.analysis_manager.recommend_safety_improvements(analysis_id, "Install speed bumps.")
        self.assertIn(improvement_id, self.analysis_manager.improvements)

if __name__ == '__main__':
    unittest.main()
