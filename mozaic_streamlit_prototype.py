import streamlit as st

# Hardcoded example audit data from the sample report
def get_hardcoded_audit_data():
    return {
        "Hospital Identification": {
            "Name": "Swiss Medical Center",
            "Location": "Zurich, Switzerland",
            "Type": "General Hospital"
        },
        "Audit Scope and Objectives": {
            "Areas Audited": "Operating Theatres, Patient Safety, Staff Procedures",
            "Purpose": "Ensure compliance with Swiss healthcare standards and improve patient safety."
        },
        "Findings and Observations": {
            "Compliance": "Mostly compliant with minor deficiencies",
            "Deficiencies": "Some staff were not consistently following hand hygiene protocols.",
            "Best Practices": "Usage of advanced surgical tools and a well-coordinated emergency protocol."
        },
        "Recommendations": {
            "Improvements": "Increase training frequency for hygiene protocols.",
            "Actions": "Assign a dedicated compliance officer to monitor adherence.",
            "Timelines": "Full implementation within 6 months."
        },
        "Compliance Status": {
            "Overall Rating": "High compliance",
            "Non-Compliance Areas": "Hand hygiene protocol, shift handovers"
        },
        "Follow-up Actions": {
            "Re-audits": "Scheduled in 1 year",
            "Monitoring Plans": "Quarterly internal reviews",
            "Deadlines": "Final deadline for full compliance: December 2024"
        }
    }

def display_audit_data(data):
    st.header("Extracted Information")

    st.subheader("Hospital Identification")
    st.write(f"Name: {data['Hospital Identification']['Name']}")
    st.write(f"Location: {data['Hospital Identification']['Location']}")
    st.write(f"Type: {data['Hospital Identification']['Type']}")

    st.subheader("Audit Scope and Objectives")
    st.write(f"Areas Audited: {data['Audit Scope and Objectives']['Areas Audited']}")
    st.write(f"Purpose: {data['Audit Scope and Objectives']['Purpose']}")

    st.subheader("Findings and Observations")
    st.write(f"Compliance: {data['Findings and Observations']['Compliance']}")
    st.write(f"Deficiencies: {data['Findings and Observations']['Deficiencies']}")
    st.write(f"Best Practices: {data['Findings and Observations']['Best Practices']}")

    st.subheader("Recommendations")
    st.write(f"Improvements: {data['Recommendations']['Improvements']}")
    st.write(f"Actions: {data['Recommendations']['Actions']}")
    st.write(f"Timelines: {data['Recommendations']['Timelines']}")

    st.subheader("Compliance Status")
    st.write(f"Overall Rating: {data['Compliance Status']['Overall Rating']}")
    st.write(f"Non-Compliance Areas: {data['Compliance Status']['Non-Compliance Areas']}")

    st.subheader("Follow-up Actions")
    st.write(f"Re-audits: {data['Follow-up Actions']['Re-audits']}")
    st.write(f"Monitoring Plans: {data['Follow-up Actions']['Monitoring Plans']}")
    st.write(f"Deadlines: {data['Follow-up Actions']['Deadlines']}")

def main():
    st.title("Prototype")
    st.title("AI - powered Audit Insights")

    # File uploader to simulate future extraction capability
    uploaded_file = st.file_uploader("Upload an Audit PDF", type="pdf")

    # Display hardcoded audit data as a prototype
    st.info("This is a prototype, showing a hardcoded example audit below.")
    audit_data = get_hardcoded_audit_data()
    display_audit_data(audit_data)

if __name__ == "__main__":
    main()
