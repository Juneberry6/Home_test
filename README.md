# Home_test
Setting up Git

import { MarkdownToMatrix } from "react-markdown-to-matrix";

export const App: React.FC = () => {
  return (
    <MarkdownToMatrix
      title="Markdown-To-Matrix"
      enabledOptions={["diff", "filters", "displayMode", "upload"]}
    />
  );
};

\begin{matrix}
  a & b \\
  f & g \\
 \end{matrix}
