const BASE_URL = "http://127.0.0.1:8000";

export async function sendMessage(message, userId = "user1") {
  const res = await fetch(`${BASE_URL}/chat`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      user_id: userId,
      message,
    }),
  });

  if (!res.ok) {
    throw new Error("Failed to connect");
  }

  return await res.json();
}

export async function uploadImages(files, message, userId = "user1") {
  const formData = new FormData();

  formData.append("user_id", userId);
  formData.append("message", message);

  files.forEach((file) => {
    formData.append("images", file);
  });

  const res = await fetch(`${BASE_URL}/upload`, {
    method: "POST",
    body: formData,
  });

  if (!res.ok) {
    throw new Error("Upload failed");
  }

  return await res.json();
}