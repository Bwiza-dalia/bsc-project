import streamlit as st
from data import dataset
from matplotlib import pyplot as plt


dataframe = dataset()

def sales_section():
    st.title("data visualization")
    st.markdown("##")


    left_column, middel_column, right_column = st.columns(3)
    with left_column:
        st.subheader("Total Orders")
        st.metric(label="", value="{:,}".format(dataframe.sales.OrderNumber.count()))
        st.markdown("""---""")
    with middel_column:
        st.subheader("Total Revenue")
        st.metric(label="", value="{:,} RWF".format(dataframe.sales.Total.sum()))
        st.markdown("""---""")
    with right_column:
        st.subheader("Total Profit")
        st.metric(label="", value="{:,} RWF".format(dataframe.sales.Profit.sum()))
        st.markdown("""---""")


    
    st.text('Bellow is a sneak peak on to our dataset')
    st.dataframe(dataframe.sales.head())
    st.markdown("""---""") 
    st.text('Bellow we analyse best months for sales and worst months for sales')
    st.line_chart(dataframe.best_months_df)
    st.markdown("""---""") 
    st.text('Bellow we analyse best district for sales')
    st.line_chart(dataframe.best_district_df)
    st.markdown("""---""") 
    st.text("Given that the best selling site has the id 284 from the district of Rwamagana.")
    #st.text('Given that the best selling site has the id: {0} from the distric of {1}'.format(dataframe.best_district_df.idxmax(), dataframe.sites.iloc[dataframe.best_district_df.idxmax()]))
    st.text("Bellow is the are best selling product from the best site")
    st.dataframe(dataframe.best_district_products)
    st.text("Bellow we shall showcase product sales per month")
    st.dataframe(dataframe.bv)
    labels = dataframe.bv.index
    sizes = dataframe.bv

    fig, ax = plt.subplots(figsize=(10,10))
    ax.pie(sizes, labels=labels, autopct="%1.1f%%")
    ax.axis("equal")

    st.pyplot(fig)
    st.markdown("""---""") 
    # st.text("shows products that sold on same date")
    # st.dataframe(dataframe.daf.head())
    
def customers_section():

    pass

def products_section():
    pass