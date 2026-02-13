This python script use DEAP (Distributed Evolutionary Algorithms) library to perform a genetic algorithm-based feature selection.  

The evaluate function serves as the fitness function. It takes an individual "Column" (a binary string representing the feature selection) as input and evaluates its fitness by performing a random mix of mathematical operations on the selected columns (It is interesting to add columns values and shuffle columns to increase performance). The fitness value is calculated as the mean squared error (MSE) between the resulting values and a selected column. Various operators such as addition, multiply, division are registered.  

The script keeps track of the best individual (with the lowest fitness) and its corresponding column selected and operators throughout the evolutionary process. After the evolutionary process is complete, the script prints the results. It displays the individuals in the Hall of Fame (selected columns), the best individual (selected columns), the selected operators used by the best individual, and the fitness obtained by the best individual.  

<rect x="28" y="92" width="324" height="180" class="opbox"/>
<g font-family="Fira Code, monospace" font-size="12">
  <text x="40" y="110" fill="#9ad0ff"># Individual = binary string (columns)</text>
  <text x="40" y="130" fill="#cfe4ff">def evaluate(individual):</text>
  <text x="64" y="150" fill="#dff5ff">selected = select\_columns(individual)</text>
  <text x="64" y="170" fill="#dff5ff">mix = random\_ops(selected)</text>
  <text x="64" y="190" fill="#dff5ff">mse = mean\_squared\_error(mix, target)</text>
  <text x="64" y="210" fill="#ffd8a8">return mse,</text>
</g>

<g transform="translate(24,64)">
  <g>
    <rect x="0" y="0" width="44" height="180" fill="#06293b" rx="6" />
    <text x="22" y="-8" class="sans" font-size="12" text-anchor="middle" fill="#9fb4d6">Columns</text>

    <g font-family="Fira Code, monospace" font-size="11" fill="#cfe4ff">
      <rect x="6" y="10" width="32" height="12" rx="4" fill="#193b54"/>
      <rect x="6" y="30" width="32" height="12" rx="4" fill="#265c7b"/>
      <rect x="6" y="50" width="32" height="12" rx="4" fill="#1f4f6a"/>
      <rect x="6" y="70" width="32" height="12" rx="4" fill="#2a6a86"/>
      <rect x="6" y="90" width="32" height="12" rx="4" fill="#17465a"/>
      <rect x="6" y="110" width="32" height="12" rx="4" fill="#2b6b88"/>
      <rect x="6" y="130" width="32" height="12" rx="4" fill="#1c4d63"/>
      <rect x="6" y="150" width="32" height="12" rx="4" fill="#27607a"/>
    </g>
  </g>

  <g transform="translate(70,6)">
    <text class="sans" x="0" y="12" font-size="12" fill="#bfe0ff">Individual (binary)</text>
    <rect x="0" y="18" width="220" height="28" rx="6" fill="#021827" stroke="#0d394f"/>
    <text x="8" y="38" class="mono" font-size="14">1 0 1 1 0 0 1 0</text>
  </g>

  <g transform="translate(70,64)">
    <text class="sans" x="0" y="12" font-size="12" fill="#bfe0ff">Operators (random mix)</text>
    <rect x="0" y="18" width="220" height="136" rx="8" fill="#011826" stroke="#0d394f"/>
    <g font-family="Fira Code, monospace" font-size="13" fill="#dff5ff">
      <g transform="translate(12,38)">
        <rect x="0" y="0" width="66" height="28" rx="6" fill="#09334d"/>
        <text x="33" y="19" text-anchor="middle">+</text>
        <rect x="82" y="0" width="66" height="28" rx="6" fill="#0b4b6b"/>
        <text x="115" y="19" text-anchor="middle">*</text>
        <rect x="164" y="0" width="66" height="28" rx="6" fill="#083c57"/>
        <text x="197" y="19" text-anchor="middle">/</text>
      </g>

      <text x="12" y="86" font-size="12" fill="#9fb4d6">shuffle, add, multiply, divide...</text>
    </g>
  </g>
</g>

<text x="28" y="84" class="mono" font-size="12" fill="#bfe0ff">Hall of Fame</text>
<g transform="translate(28,92)" font-family="Fira Code, monospace" font-size="12">
  <rect x="0" y="0" width="320" height="42" rx="6" fill="#042e42" stroke="#0b4b6b"/>
  <text x="12" y="26" fill="#dff5ff">[1 0 1 1 0 0 1 0]  [0.12]</text>
</g>

<text x="28" y="152" class="mono" font-size="12" fill="#bfe0ff">Best Individual</text>
<g transform="translate(28,160)" font-family="Fira Code, monospace" font-size="12">
  <rect x="0" y="0" width="320" height="42" rx="6" fill="#032a3c" stroke="#0b4b6b"/>
  <text x="12" y="26" fill="#7ee3a6">[1 0 1 1 0 0 1 0]</text>
</g>

<text x="28" y="222" class="mono" font-size="12" fill="#bfe0ff">Selected Operators</text>
<g transform="translate(28,230)" font-family="Fira Code
