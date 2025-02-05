import React from "react";
import { Button } from "../node_modules/mui/material";

const HomePage: React.FC = () => {
  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100 p-4">
      <h1 className="text-4xl font-bold text-gray-900">Welcome to Cardify</h1>
      <p className="text-lg text-gray-600 mt-2">Card Scanner and Value Evaluator</p>
      <Button className="mt-4 px-6 py-2 text-lg">Login</Button>
    </div>
  );
};

export default HomePage;
