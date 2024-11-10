import streamlit as st
# from streamlit_lottie import st_lottie
import json
import requests

# Set page configuration
st.set_page_config(
    page_title="Home$crapper - Sustainable Waste Management",
    page_icon="♻️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# # Function to load Lottie animations from URL
# def load_lottieurl(url: str):
#     """ Loads a Lottie animation from a URL.
    
#     Parameters:
#         url (str): The URL of the Lottie JSON file.
        
#     Returns:
#         dict: The Lottie animation JSON data or None if the request fails.
#     """
#     r = requests.get(url)
#     if r.status_code != 200:
#         return None
#     return r.json()

# Define each page as a separate function
def home():
    st.title("♻️ *Welcome to Home$crapper!*")
    st.markdown("### Your Sustainable Waste Management Solution")
    st.write("---")
    
    st.markdown("""
        *Home Scrapper* is an innovative platform connecting households and vendors to promote responsible recycling and waste management. 
        Our mission is to help users turn recyclable waste into value, ensuring proper and sustainable disposal. 
        Our platform also facilitates a marketplace where users can donate or sell reusable items at minimal cost, making Home$crapper an eco-friendly and socially impactful choice.
    """)
    
    st.write("---")
    st.header("🔑 *Key Features*")
    st.markdown("""
        - *Trusted Vendors*: Connect with genuine, vetted vendors.
        - *Real-Time Pricing*: Access current market rates for waste materials.
        - *Verified Weighing Machines*: Ensure accurate weights for transparency.
        - *Marketplace for Donations and Resales*: Donate or sell reusable goods.
        - *Secure Transactions*: Reliable interactions between users and vendors.
    """)
    
    st.write("---")
    st.header("🚀 *How It Works*")
    
    with st.expander("♻️ Recycling Waste"):
        st.markdown("""
            1. *Select Waste Type*: Choose the recyclable waste you want to dispose of.
            2. *Find a Vendor*: View nearby vendors offering competitive prices.
            3. *Schedule Pickup*: Select a vendor and set a pickup date.
            4. *Receive Payment*: Get paid based on weight and market rate.
        """)
    
    with st.expander("👐 Donate or Resell Goods"):
        st.markdown("""
            1. *List an Item*: Post items for donation or minimal sale.
            2. *Connect with a Buyer/Recipient*: Interested parties reach out.
            3. *Arrange Pickup or Delivery*: Hand over the item directly.
        """)
    
    st.write("---")
    st.header("📈 *Get Started*")
    st.markdown("""
        Ready to turn waste into value? *[Join Home$crapper today](#)* to start recycling responsibly or donating unused items with ease.
    """)
    
    st.button("🚀 *Join Now*", help="Click to sign up and start your eco-friendly journey with Home$crapper!")

def frontend():
    st.title("📄 *Frontend Documentation*")
    st.write("---")
    
    st.subheader("🛠️ *Design Considerations*")
    st.markdown("""
        The frontend of the *Home$crapper* project was designed with several key considerations in mind:
        - *User-Centric Design*: The interface prioritizes ease of use, ensuring that users can navigate the platform effortlessly to either list items for sale or browse available products.
        - *Responsive Layout*: The application is built to be fully responsive, providing a seamless experience across various devices, including desktops and tablets.
        - *Accessibility*: Adhering to accessibility standards ensures that the application is usable by individuals with disabilities, enhancing usability for all users.
        - *Performance Optimization*: The frontend is optimized for performance, minimizing load times and ensuring smooth interactions through efficient rendering and state management.
    """)
    
    st.subheader("⭐ *Key Features*")
    st.markdown("""
        The frontend of *Home$crapper* includes several notable features:
        - *Authentication*: Users can easily log in and manage their profiles through a secure authentication process using Auth0.
        - *Marketplace Functionality*: Users can list items for sale, view details of listed products, and make purchases directly through the platform.
        - *Garbage Scrapping Interface*: A dedicated section for users to report garbage or unwanted materials, facilitating community engagement in environmental efforts.
        - *Dynamic Content Loading*: The application dynamically loads content based on user interactions, providing a smooth and engaging experience without full page reloads.
        - *VoiceFlow ChatBot Service*: Enhances the user experience by providing answers to queries, adding to user satisfaction.
    """)
    
    st.subheader("🧰 *Technological Stack*")
    st.markdown("""
        The *Home$crapper* frontend utilizes a modern technological stack:
        - *React*: A JavaScript library for building user interfaces, allowing for the creation of reusable UI components.
        - *Vite*: A build tool that provides a fast development environment with hot module replacement (HMR).
        - *Material UI*: A popular React UI framework that offers pre-designed components to speed up development and ensure a consistent look and feel.
        - *Emotion*: A CSS-in-JS library used for styling components dynamically based on props and state.
        - *React Router*: A routing library for React that enables navigation between different views in the application.
    """)
    
    st.subheader("📜 *Technical Documentation*")
    st.markdown("""
        *Project Structure:*
        
        ```
        competition/
            ├── eslint.config.js
            ├── index.html
            ├── package-lock.json
            ├── package.json
            └── public/
                └── vite.svg
                └── README.md
                └── src/
                    ├── App.css
                    ├── App.jsx
                    ├── assets/
                    │   ├── hero.png
                    │   ├── logo.png
                    │   └── profile.png
                    ├── components/
                    │   └── Profile.jsx
                    ├── hooks/
                    │   └── usePreviewImg.jsx
                    ├── index.css
                    └── main.jsx
                    └── pages/
                        ├── Appbar.jsx
                        ├── Contact.jsx
                        ├── Hero.jsx
                        ├── HomeOptions.jsx
                        ├── Login.jsx
                        ├── Logout.jsx
                        ├── MyProfile.jsx
                        ├── Orders.jsx
                        └── part1/
                            ├── Final.jsx
                            ├── ModalData.jsx
                            ├── ProductList.jsx
                            ├── Seller.jsx
                            ├── Vendor.jsx
                            └── VendorList.jsx
                        └── part2/
                            ├── Buyer.jsx
                            └── Seller.jsx
                            └── ProductList.jsx 
            vite.config.js 
        ```

        **Key Files:**
        
        1. **index.html**: The entry point of the application. It includes meta tags for responsiveness and links to the main JavaScript file.

            ```html
            <!doctype html>
            <html lang="en">
              <head>
                <meta charset="UTF-8" />
                <link rel="icon" type="image/svg+xml" href="/vite.svg" />
                <meta name="viewport" content="width=device-width, initial-scale=1.0" />
                <title>Home$crapper</title>
              </head>
              <body>
                <div id="root"></div>
                <script type="module" src="/src/main.jsx"></script>
              </body>
            </html>
            ```

        2. **main.jsx**: Initializes the React application and renders it into the DOM, using Auth0Provider, RecoilRoot, and StrictMode for enhanced setup.

            ```javascript
            import { StrictMode } from 'react';
            import { createRoot } from 'react-dom/client';
            import { Auth0Provider } from '@auth0/auth0-react';
            import './index.css';
            import App from './App.jsx';
            import { RecoilRoot } from 'recoil';

            createRoot(document.getElementById('root')).render(
              <Auth0Provider 
                domain="dev-ob2zgf2rb2cj4emu.us.auth0.com" 
                clientId="PKriUy3BJCzcEQzBVZGG0dKjlCaXEyEs"
                authorizationParams={{ redirect_uri: window.location.origin }}
              >
                <StrictMode>
                  <RecoilRoot>
                    <App />
                  </RecoilRoot>
                </StrictMode>
              </Auth0Provider>
            );
            ```

        3. **App.jsx**: The root component that manages routing and layout.

        4. **Components Directory (src/components/)**: Contains reusable components such as Profile.jsx, which displays user profile information.

        5. **Pages Directory (src/pages/)**: Contains various page components like Hero, Login, Logout, etc., each responsible for rendering specific parts of the application.

        **Styling**: The application uses **CSS Modules** and **Emotion** for styling:
        
        - **CSS Modules**: Styles are scoped locally to avoid conflicts between different components.
        - **Emotion**: Provides dynamic styling capabilities based on component props.

        **ESLint Configuration**: The project uses **ESLint** to maintain code quality. The configuration file (eslint.config.js) sets up rules specific to React development:

            ```javascript
            import js from '@eslint/js';
            import globals from 'globals';
            import react from 'eslint-plugin-react';
            import reactHooks from 'eslint-plugin-react-hooks';
            import reactRefresh from 'eslint-plugin-react-refresh';

            export default [
              {
                ignores: ['dist'],
              },
              {
                files: ['/.{js,jsx}'],
                languageOptions: {
                  ecmaVersion: 2020,
                  globals: globals.browser,
                  parserOptions: {
                    ecmaVersion: 'latest',
                    ecmaFeatures: {
                      jsx: true,
                    },
                    sourceType: 'module',
                  },
                },
                settings: {
                  react: {
                    version: '18.3',
                  },
                },
                plugins: {
                  react,
                  'react-hooks': reactHooks,
                  'react-refresh': reactRefresh,
                },
                rules: {
                  ...js.configs.recommended.rules,
                  ...react.configs.recommended.rules,
                  ...react.configs['jsx-runtime'].rules,
                  ...reactHooks.configs.recommended.rules,
                  'react/jsx-no-target-blank': 'off',
                  'react-refresh/only-export-components': ['warn', { allowConstantExport: true }],
                },
              },
            ];
        
        **Conclusion**: This documentation provides a comprehensive overview of the frontend design considerations, key features, technological stack, and technical structure of the *Home$crapper* project. By adhering to these guidelines and utilizing modern technologies, the project aims to create an efficient platform for scrapping garbage and facilitating second-hand transactions.
    """)

def backend():
    st.title("📄 *Backend Documentation*")
    st.write("---")
    
    st.subheader("🔧 *Design Considerations*")
    st.markdown("""
        The backend of the *Home$crapper* project was developed with several design considerations to ensure robustness, scalability, and security:
        - *Modular Architecture*: Structured in a modular fashion, allowing for easy maintenance and scalability. Each component (controllers, models, routes) is separated to enhance code readability and organization.
        - *Security*: Implementing JWT (JSON Web Tokens) for authentication ensures that user sessions are secure. Additionally, sensitive data is managed through environment variables using dotenv.
        - *Database Connection Management*: Utilizes Mongoose for MongoDB interactions, ensuring efficient database connection handling and schema validation.
        - *Error Handling*: Comprehensive error handling mechanisms are implemented to provide meaningful responses to the client while logging errors for debugging purposes.
    """)
    
    st.subheader("⭐ *Key Features*")
    st.markdown("""
        The backend of *Home$crapper* includes several essential features:
        - *User Authentication*: Users can register and log in securely, with their credentials stored safely in the database.
        - *Product Management*: Supports CRUD operations for products, allowing sellers to add, update, and delete their listings.
        - *Buyer and Seller Profiles*: Separate models for buyers and sellers enable tailored functionalities according to user roles.
        - *Cloud Storage Integration*: Integration with Cloudinary allows for image uploads and management directly from the application.
        - *Feedback Mechanism*: Users can provide feedback on products, which is processed and stored for future reference.
    """)
    
    st.subheader("🛠️ *Technological Stack*")
    st.markdown("""
        The backend of *Home$crapper* employs a modern technological stack:
        - *Node.js*: A JavaScript runtime that allows for server-side scripting.
        - *Express.js*: A web application framework for Node.js that simplifies routing and middleware management.
        - *MongoDB*: A NoSQL database used for storing user and product data.
        - *Mongoose*: An ODM (Object Data Modeling) library for MongoDB that provides schema-based solutions to model application data.
        - *Cloudinary*: A cloud service for image upload and management.
        - *JWT (JSON Web Tokens)*: Used for secure authentication.
    """)
    
    st.subheader("📜 *Technical Documentation*")
    st.markdown("""
        *Project Structure:*
        
        ```
        backend/
            ├── app.js
            ├── controller/
            │   └── User.js
            ├── db/
            │   └── connectDB.js
            ├── middleware/
            │   └── protectRoute.js
            ├── model/
            │   ├── Buyer.js
            │   ├── Product.js
            │   └── Seller.js
            ├── package-lock.json
            ├── package.json
            ├── Routes/
            │   └── userRouter.js
            └── utils/
                └── helper/
                    └── cookies.js
        ```

        **Key Files:**
        
        1. **app.js**: The main entry point of the application that initializes the server and connects to the database.

            ```javascript
            import express from "express";
            import dotenv from "dotenv";
            import cookieParser from "cookie-parser";
            import connectDB from "./db/connectDB.js";
            import { v2 as cloudinary } from "cloudinary";
            import userRouter from "./Routes/userRouter.js";

            dotenv.config();
            connectDB();

            cloudinary.config({
                cloud_name: process.env.CLOUD_NAME,
                api_key: process.env.CLOUD_API_KEY,
                api_secret: process.env.CLOUD_API_SECRET,
            });

            const app = express();
            app.use(cookieParser());
            app.use(express.json({ limit: "50mb" }));
            app.use(express.urlencoded({ extended: true }));
            app.use("/api/user", userRouter);

            const PORT = process.env.PORT || 3000;
            app.listen(PORT, () => {
                console.log("Server started on port " + PORT);
            });
            ```

        2. **connectDB.js**: Handles the connection to MongoDB.

            ```javascript
            import mongoose from "mongoose";

            const connectDB = async () => {
                try {
                    const conn = await mongoose.connect(process.env.MONGODB_URL);
                    console.log(`MongoDB connected: ${conn.connection.host}`);
                } catch (error) {
                    console.log(`Error: ${error.message}`);
                    process.exit(1);
                }
            };

            export default connectDB;
            ```

        3. **Controllers (controller/User.js)**: Manages user-related operations such as registration, profile updates, and product management.

           **Updated Adduser Controller Code:**

           ```javascript
           const Adduser = async (req, res) => {
               try {
                   const { email } = req.body;
                   console.log("Working:", req.body);
                   if (!email) {
                       return res.status(400).json({ message: "All fields are required" });
                   }
                   const buyer = await Buyer.create({ email });
                   const seller = await Seller.create({ email });
                   if (buyer && seller) {
                       generateTokenAndSetCookie(buyer._id, res);
                       generateTokenAndSetCookie(seller._id, res);
                   }
                   res.status(201).json({ buyer, seller });
               } catch (error) {
                   console.log(error);
                   res.status(500).json({ message: error.message });
               }
           };
           ```

        4. **Models (model/)**:
           - **Buyer.js**: Defines the Buyer schema with fields like name, email, password, etc.
           - **Seller.js**: Defines the Seller schema similar to Buyer but includes additional fields relevant to sellers.
           - **Product.js**: Defines the Product schema including details like name, description, price, image array, etc.

        5. **Middleware (middleware/protectRoute.js)**: Protects routes by verifying JWT tokens to ensure that only authenticated users can access certain endpoints.

        **Error Handling**: The backend implements error handling in various parts of the code. For example, in the Adduser controller function provided above, we handle missing fields and log errors.

        **Conclusion**: This documentation provides a comprehensive overview of the backend design considerations, key features, technological stack, and technical structure of the *Home$crapper* project. By following these guidelines and utilizing modern technologies, the project aims to create a secure and efficient platform for managing scrapping operations and facilitating second-hand transactions.
    """)

def GenAI_and_machine_learning():
    st.title("🤖 *GenAI and Machine Learning Documentation*")
    st.write("---")
    
    st.subheader("🔍 *Overview*")
    st.markdown("""
        The *Home$crapper* platform integrates advanced machine learning and generative AI technologies to enhance user experience, optimize waste management processes, and promote sustainable practices. 
        This section outlines the design considerations, key features, and technological stack used in implementing these functionalities.
    """)
    
    st.subheader("🛠️ *Design Considerations*")
    st.markdown("""
        The integration of machine learning and generative AI in the *Home$crapper* project was guided by several key design considerations:
        - *Scalability*: The architecture is designed to handle increasing data volumes as more users engage with the platform, ensuring that machine learning models can scale accordingly.
        - *Data Privacy*: User data is handled securely, with anonymization techniques applied to protect personal information while still enabling effective model training.
        - *Real-Time Processing*: Implementing real-time data processing capabilities allows for immediate feedback and recommendations to users based on their interactions with the platform.
        - *Continuous Learning*: The system is designed to continuously learn from new data inputs, improving model accuracy over time through retraining mechanisms.
    """)
    
    st.subheader("⭐ *Key Features*")
    st.markdown("""
        The machine learning and generative AI components of *Home$crapper* offer several innovative features:
        - *Personalized Recommendations*: Utilizing collaborative filtering algorithms to suggest vendors or products based on user preferences and behaviors.
        - *Image Recognition*: Implementing computer vision techniques to automatically classify waste types from user-uploaded images, streamlining the recycling process.
        - *Natural Language Processing (NLP)*: Enhancing user interactions through chatbots that can understand and respond to user queries in natural language.
        - *Predictive Analytics*: Analyzing historical data to forecast waste generation patterns, helping users plan better for waste disposal.
    """)
    
    st.subheader("📊 *Technological Stack*")
    st.markdown("""
        The following technologies were utilized for implementing machine learning and generative AI functionalities:
        - *Python*: The primary programming language for developing machine learning models using libraries such as TensorFlow and scikit-learn.
        - *Pandas*: For data manipulation and analysis, making it easier to preprocess data before feeding it into machine learning models.
        - *NumPy*: A library for numerical computations that supports large multi-dimensional arrays and matrices.
        - *OpenCV*: Used for image processing tasks related to waste classification.
        - *NLTK / SpaCy*: Libraries for natural language processing tasks, enabling chatbot functionalities and text analysis.
        - *Flask / FastAPI*: Frameworks used to build RESTful APIs that serve machine learning models, allowing seamless integration with the frontend application.
    """)
    
    st.subheader("📜 *Model Training and Evaluation*")
    st.markdown("""
        The machine learning models are trained using a systematic approach:
        
        1. **Data Collection**: Gathering relevant datasets from user interactions, vendor information, and historical waste management data.
        
        2. **Data Preprocessing**: Cleaning and preparing the data for training by handling missing values, normalizing data, and encoding categorical variables.
        
        3. **Model Selection**: Choosing appropriate algorithms based on the problem domain (e.g., classification for image recognition, regression for predictive analytics).
        
        4. **Training**: Utilizing training datasets to train models while monitoring performance metrics such as accuracy, precision, recall, and F1 score.
        
        5. **Evaluation**: Validating model performance using test datasets and applying techniques like cross-validation to ensure robustness.
        
        6. **Deployment**: Once validated, models are deployed via APIs for real-time inference within the application.
        
        7. **Monitoring**: Continuously monitoring model performance post-deployment to identify any degradation in accuracy over time due to changing user behaviors or data distributions.
    """)
    
    st.subheader("🚀 *Future Enhancements*")
    st.markdown("""
        Looking ahead, several enhancements are planned for the GenAI and machine learning components:
        - **Enhanced Image Classification**: Improving image recognition capabilities with advanced deep learning architectures such as Convolutional Neural Networks (CNNs).
        - **User Feedback Loop**: Incorporating user feedback mechanisms to refine model outputs based on real-world usage.
        - **Integration of External Data Sources**: Utilizing external datasets (e.g., weather patterns) to improve predictive analytics related to waste generation forecasts.
    """)

    st.write("---")

# Define the navigation sidebar
def navigation():
    st.sidebar.title("Navigation")
    pages = {
        "Home": home,
        "Frontend Documentation": frontend,
        "Backend Documentation": backend,
        "GenAI and Machine Learning": GenAI_and_machine_learning,
    }
    
    selection = st.sidebar.radio("Go to", list(pages.keys()))
    
    # Call the selected page function
    pages[selection]()

# Call the home function to display the home page
if __name__ == "__main__":
    navigation()