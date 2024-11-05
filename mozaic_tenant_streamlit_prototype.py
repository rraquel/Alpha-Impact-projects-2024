import streamlit as st
import matplotlib.pyplot as plt

# Define a compact metric card with optional progress bar and subtitle
def compact_metric_card(title, value, subtitle=None, progress=None):
    # Display the main title and value
    st.markdown(f"<div style='background-color: #f8f9fa; padding: 15px; border-radius: 10px; margin: 5px 0; width: 100%; box-shadow: 1px 1px 5px rgba(0, 0, 0, 0.1);'>"
                f"<p style='font-size:14px; color: #6c757d; font-weight: bold; margin-bottom: 5px;'>{title}</p>"
                f"<p style='font-size:20px; color: #007bff; margin-top: 0; margin-bottom: 5px;'>{value}</p>", 
                unsafe_allow_html=True)

    # Conditionally render the progress bar if a value is provided
    if progress is not None:
        st.markdown(
            f"<div style='background-color: #d9edf7; border-radius: 5px; overflow: hidden; width: 100%;'>"
            f"<div style='width: {progress}%; background-color: #007bff; height: 8px;'></div>"
            "</div>", 
            unsafe_allow_html=True
        )

    # Conditionally render the subtitle if provided and non-empty
    if subtitle:
        st.markdown(f"<p style='font-size:12px; color: #6c757d; margin-top: 8px;'>{subtitle}</p>", unsafe_allow_html=True)

    # Close the main div for styling
    st.markdown("</div>", unsafe_allow_html=True)

# Function to create a compact donut chart for satisfaction rate
def create_donut_chart(value, label):
    fig, ax = plt.subplots(figsize=(1, 1))
    ax.pie([value, 100 - value], labels=["", ""], startangle=90, colors=["#007bff", "#f0f2f6"], 
           wedgeprops=dict(width=0.3, edgecolor='w'))
    ax.text(0, 0, f"{value}%", ha='center', va='center', fontsize=10, color="#007bff")
    ax.set_title(label, fontsize=10, color="#6c757d")
    plt.axis("equal")
    return fig

# Main function to render the dashboard
def main():
    st.title("MoZaïC Tenant Analysis Dashboard")
    st.markdown("<hr style='border: 1px solid #007bff;'>", unsafe_allow_html=True)

    # Dropdown menu for selecting the center
    center = st.selectbox("Select Center for Analysis:", ["Swiss Medical Center - Zurich", "Geneva Health Clinic", "Bern Regional Hospital"])
    st.write(f"**Currently Viewing:** {center}")

    # Organize layout in rows and columns for better alignment and compact view
    col1, col2, col3 = st.columns(3)

    # Hospital Overview Section
    with col1:
        st.markdown("<h3 style='color: #4b4f56;'>Hospital Overview</h3>", unsafe_allow_html=True)
        compact_metric_card("Hospital Name", "Swiss Medical Center")
        compact_metric_card("Location", "Zurich, Switzerland")
        compact_metric_card("Type", "General Hospital")
        compact_metric_card("Operational Capacity", "85%", progress=85)
        compact_metric_card("Website", "[Visit SMC](https://www.swissmedicalcenter.com/)")

    # Operational Metrics Section
    with col2:
        st.markdown("<h3 style='color: #4b4f56;'>Operational Metrics</h3>", unsafe_allow_html=True)
        compact_metric_card("Annual Patient Volume", "120,000 patients")
        compact_metric_card("Bed Capacity", "200 beds")
        compact_metric_card("Staff Count", "500+")
        compact_metric_card("Avg. Wait Time", "15 minutes", progress=75)

    # Financial Performance Section
    with col3:
        st.markdown("<h3 style='color: #4b4f56;'>Financial Performance</h3>", unsafe_allow_html=True)
        compact_metric_card("Annual Revenue", "CHF 50 million")
        compact_metric_card("Profit Margin", "10%", progress=10)
        compact_metric_card("Recent Investments", "CHF 5 million")
        compact_metric_card("YoY Growth", "+8%", subtitle="Compared to last year")

    st.markdown("<hr style='border: 1px solid #007bff;'>", unsafe_allow_html=True)

    # Compliance & Patient Satisfaction Section
    col4, col5 = st.columns([2, 1])

    with col4:
        st.markdown("<h3 style='color: #4b4f56;'>Compliance & Accreditation</h3>", unsafe_allow_html=True)
        compact_metric_card("Accreditation", "ISO 9001 certified")
        compact_metric_card("Last Audit Date", "January 2023")
        compact_metric_card("Compliance Rating", "High (90%)", progress=90)
        compact_metric_card("Safety Incidents", "3 incidents", subtitle="Non-critical")

    with col5:
        st.markdown("<h3 style='color: #4b4f56;'>Patient Satisfaction</h3>", unsafe_allow_html=True)
        satisfaction_chart = create_donut_chart(92, "Satisfaction Rate")
        st.pyplot(satisfaction_chart)
        compact_metric_card("Complaints per Month", "15", subtitle="Avg. complaints reported")
        compact_metric_card("Repeat Patients", "75%", subtitle="Patients returning for care")
        compact_metric_card("NPS Score", "82", subtitle="Net Promoter Score")

    st.markdown("<hr style='border: 1px solid #007bff;'>", unsafe_allow_html=True)

    # Patient Demographics & Risk Assessment Section
    col6, col7 = st.columns(2)

    with col6:
        st.markdown("<h3 style='color: #4b4f56;'>Patient Demographics</h3>", unsafe_allow_html=True)
        compact_metric_card("Average Age", "45 years")
        compact_metric_card("Female Patients", "54%")
        compact_metric_card("Out-of-Town Patients", "30%", subtitle="Non-local patients")
        compact_metric_card("Insurance Coverage", "92%", subtitle="With insurance")

    with col7:
        st.markdown("<h3 style='color: #4b4f56;'>Risk Assessment</h3>", unsafe_allow_html=True)
        compact_metric_card("Identified Risks", "Minor hygiene lapses")
        compact_metric_card("Mitigation Plan", "Training & Staffing")
        compact_metric_card("Timeline", "6 months")
        compact_metric_card("Follow-up Audit", "Scheduled for Jan 2025")

    # Style adjustments for footer
    st.markdown(
        """
        <style>
        .footer {position: fixed; bottom: 0; width: 100%; background-color: #f8f9fa; padding: 5px; text-align: center; color: #6c757d; font-size: 12px;}
        </style>
        <div class="footer">© 2024 MoZaïC Asset Management | Tenant Analysis Dashboard Prototype</div>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
