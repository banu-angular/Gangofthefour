# Imagine a Tax Consultant visiting a large corporation. The corporation has many different departments (Sales, HR, R&D), each with different accounting structures. Instead of adding "CalculateTax" methods to every single department class, the Tax Consultant (the Visitor) moves through the departments and performs the specific tax calculations based on the type of department they are currently "visiting."
from abc import ABC, abstractmethod
class Department(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass
class SalesDepartment(Department):
    def accept(self, visitor):
        visitor.visit_sales_department(self)
class HRDepartment(Department):
    def accept(self, visitor):
        visitor.visit_hr_department(self)
class RnDDepartment(Department):
    def accept(self, visitor):
        visitor.visit_rnd_department(self)
class TaxConsultant:
    def visit_sales_department(self, department):
        print("Calculating tax for Sales Department.")
    def visit_hr_department(self, department):
        print("Calculating tax for HR Department.")
    def visit_rnd_department(self, department):
        print("Calculating tax for R&D Department.")
# Example usage
sales = SalesDepartment()
hr = HRDepartment()
rnd = RnDDepartment()
tax_consultant = TaxConsultant()
sales.accept(tax_consultant)  # Output: Calculating tax for Sales Department.
hr.accept(tax_consultant)     # Output: Calculating tax for HR Department.
rnd.accept(tax_consultant)    # Output: Calculating tax for R&D Department.
# Output:
# Calculating tax for Sales Department.
# Calculating tax for HR Department.
# Calculating tax for R&D Department.
