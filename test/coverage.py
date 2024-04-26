import sys
sys.path.append("./src")
import coverage

# Initialize coverage
cov = coverage.Coverage()
cov.start()

if __name__ == '__main__':
    # Stop coverage
    cov.stop()
    # Save coverage results
    cov.save()
    # Generate coverage report
    cov.report()