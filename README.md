# assignment# Price Comparison API

## Setup Instructions

1. Clone the repository:
    ```bash
    git clone <repository-url>
    cd price-comparison-api
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the application:
    ```bash
    uvicorn app.main:app --reload
    ```

4. Access the API documentation:
    Open your browser and go to `http://127.0.0.1:8000/docs` to see the interactive API documentation.

## Database Choice

We are using SQLite for simplicity and ease of setup. However, for a production system, a more robust database like PostgreSQL or MySQL should be considered for scalability and reliability.

## API Endpoints

1. **Search Products**:
    - **GET /api/products?name=<product_name>**
    - Returns a list of products matching the search query, including the product name, price, and retailer name.

2. **Add Product**:
    - **POST /api/products**
    - Adds a new product to the database.
    - Request body should include product name, price, and retailer name.

3. **Get All Products**:
    - **GET /api/products**
    - Returns a list of all products in the database.

## Example Requests and Responses

### Search Products
**Request**:
```bash
curl -X 'GET' \
  'http://127.0.0.1:8000/api/products?name=Product%20A' \
  -H 'accept: application/json'
Response:
[
  {
    "id": 1,
    "name": "Product A",
    "price": 100,
    "retailer_name": "store1"
  },
  {
    "id": 2,
    "name": "Product A",
    "price": 110,
    "retailer_name": "store2"
  }
]
Add Product
Request:
curl -X 'POST' \
  'http://127.0.0.1:8000/api/products' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "Product C",
  "price": 200,
  "retailer_name": "store1"
}'
Response:
{
  "id": 3,
  "name": "Product C",
  "price": 200,
  "retailer_name": "store1"
}
Challenges Faced
Setting up the project structure and ensuring all dependencies are correctly installed.
Designing the database schema and implementing the CRUD operations.
Testing the API endpoints and handling edge cases.


## Step 6: Run the Application

Start the application:

```bash
uvicorn app.main:app --reload
Open your browser and navigate to http://127.0.0.1:8000/docs to see the interactive API documentation provided by FastAPI.
