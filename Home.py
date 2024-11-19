
import { MarkdownToMatrix } from "react-markdown-to-matrix";

export const App: React.FC = () => { return ( <MarkdownToMatrix title="Markdown-To-Matrix" enabledOptions={["diff", "filters", "displayMode", "upload"]} /> ); };

\begin{matrix} a & b \ f & g \ \end{matrix}

\vec{v} = \begin{bmatrix} X \\ Y \end{bmatrix}
    
def factorial(n):
    if n == 0:
    	return 1
    else:
    	return n * factorial(n - 1)
    	
 number = 5
 result factorial(number)
 print(f"The factorial of (number) is (result).")
