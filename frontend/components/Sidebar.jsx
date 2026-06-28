import React from "react";

export default function Sidebar() {
  return (
    <div className="w-64 h-screen bg-[#171717] border-r border-gray-800 flex flex-col">
      
      {/* Top Section */}
      <div className="p-4 border-b border-gray-800">
        <h1 className="text-lg font-semibold text-white">🛡 Insurance AI</h1>

        <button className="mt-4 w-full bg-[#10a37f] hover:bg-[#0e8f6f] text-white py-2 rounded-lg">
          + New Claim
        </button>
      </div>

      {/* Recent Chats */}
      <div className="flex-1 overflow-y-auto p-4 space-y-3">
        <p className="text-gray-400 text-sm"> Claims Types</p>

        <div className="space-y-2">
          <div className="p-2 rounded bg-white hover:bg-[#867575] cursor-pointer text-sm">
            🚗 Car Damage Claim
          </div>

          <div className="p-2 rounded bg-white hover:bg-[#867575] cursor-pointer text-sm">
            💻 Laptop Broken Screen
          </div>

          <div className="p-2 rounded bg-white hover:bg-[#867575] cursor-pointer text-sm">
            📦 Package Damage
          </div>
        </div>
      </div>

      {/* Bottom */}
      <div className="p-4 border-t border-gray-800">
        {/* <div className="text-sm text-gray-400">Settings</div> */}
        {/* <div className="text-sm text-gray-400 mt-2">Logout</div> */}
      </div>
    </div>
  );
}