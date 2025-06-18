# API Documentation for Metaverse Crypto 3D

## Overview

The Metaverse Crypto 3D project provides a full-stack application that integrates a 3D interactive environment using Three.js on the frontend and Reflex as the backend framework. This document outlines the API endpoints available for interacting with the backend services.

## Base URL

The base URL for all API requests is:

```
http://localhost:8000/api
```

## Endpoints

### Scene Management

#### Get Scene State

- **Endpoint:** `/scene/state`
- **Method:** `GET`
- **Description:** Retrieves the current state of the 3D scene, including objects and their properties.
- **Response:**
  ```json
  {
    "status": "success",
    "scene_data": {
      "objects": [],
      "camera_position": {"x": 0, "y": 0, "z": 5},
      "selected_object": null
    }
  }
  ```

#### Update Scene

- **Endpoint:** `/scene/update`
- **Method:** `POST`
- **Description:** Updates the scene state with new data.
- **Request Body:**
  ```json
  {
    "objects": [...],
    "camera_position": {"x": 0, "y": 0, "z": 5},
    "selected_object": "object_id"
  }
  ```
- **Response:**
  ```json
  {
    "status": "success",
    "message": "Scene updated successfully."
  }
  ```

### User Management

#### Get User Profile

- **Endpoint:** `/user/profile`
- **Method:** `GET`
- **Description:** Retrieves the profile information of the currently authenticated user.
- **Response:**
  ```json
  {
    "status": "success",
    "user": {
      "id": "user_id",
      "username": "user_name",
      "avatar": "avatar_url"
    }
  }
  ```

#### Update User Profile

- **Endpoint:** `/user/update`
- **Method:** `POST`
- **Description:** Updates the user's profile information.
- **Request Body:**
  ```json
  {
    "username": "new_username",
    "avatar": "new_avatar_url"
  }
  ```
- **Response:**
  ```json
  {
    "status": "success",
    "message": "Profile updated successfully."
  }
  ```

### Blockchain Interactions

#### Get NFT Data

- **Endpoint:** `/blockchain/nft`
- **Method:** `GET`
- **Description:** Retrieves information about NFTs owned by the user.
- **Response:**
  ```json
  {
    "status": "success",
    "nfts": [
      {
        "id": "nft_id",
        "name": "nft_name",
        "image": "nft_image_url"
      }
    ]
  }
  ```

#### Create NFT

- **Endpoint:** `/blockchain/nft/create`
- **Method:** `POST`
- **Description:** Creates a new NFT.
- **Request Body:**
  ```json
  {
    "name": "nft_name",
    "description": "nft_description",
    "image": "nft_image_url"
  }
  ```
- **Response:**
  ```json
  {
    "status": "success",
    "message": "NFT created successfully."
  }
  ```

### WebSocket Communication

#### Connect to WebSocket

- **Endpoint:** `/ws`
- **Method:** `GET`
- **Description:** Establishes a WebSocket connection for real-time communication.
- **Response:** WebSocket connection established.

## Error Handling

All API responses will include a `status` field indicating success or failure, along with a `message` field providing additional context in case of errors.

## Conclusion

This API documentation provides a comprehensive overview of the endpoints available for the Metaverse Crypto 3D project. For further details on specific endpoints or additional functionality, please refer to the source code or contact the development team.