import React, { useState } from "react";

export default function UploadArea({ onUpload }) {
  const [files, setFiles] = useState([]);

  const handleFileChange = (e) => {
    const selectedFiles = Array.from(e.target.files);
    setFiles(selectedFiles);
  };

  const handleUpload = () => {
    if (files.length === 0) return;

    onUpload(files);
    setFiles([]);
  };

  return (
    <div className="w-full p-4 border-t border-gray-800 bg-[#1f1f1f]">

      {/* Drag & Drop Box */}
      <label className="flex flex-col items-center justify-center border-2 border-dashed border-gray-600 rounded-xl p-6 cursor-pointer hover:border-[#10a37f]">
        
        <input
          type="file"
          multiple
          accept="image/*"
          className="hidden"
          onChange={handleFileChange}
        />

        <p className="text-gray-300">📷 Drag & Drop or Click to Upload</p>
        <p className="text-xs text-gray-500 mt-1">
          JPG, PNG, JPEG supported
        </p>
      </label>

      {/* Preview */}
      {files.length > 0 && (
        <div className="flex gap-2 mt-3 flex-wrap">
          {files.map((file, idx) => (
            <div
              key={idx}
              className="bg-[#2a2a2a] px-3 py-2 rounded text-xs text-white"
            >
              {file.name}
            </div>
          ))}
        </div>
      )}

      {/* Upload Button */}
      {files.length > 0 && (
        <button
          onClick={handleUpload}
          className="mt-3 bg-[#10a37f] px-4 py-2 rounded text-white hover:bg-[#0e8f6f]"
        >
          Upload Images
        </button>
      )}
    </div>
  );
}