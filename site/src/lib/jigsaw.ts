export type EdgeShape = 'flat' | 'tab' | 'blank';
// export type RevealOrder = 'row' | 'center' | 'spiral' | 'random'; // No longer needed
export interface EdgeSet {
  top: EdgeShape;
  right: EdgeShape;
  bottom: EdgeShape;
  left: EdgeShape;
}

function lcg(seed: number): () => number {
  let s = seed;
  return () => {
    s = (s * 1103515245 + 12345) % 2147483648;
    return s / 2147483648; // Returns 0..1
  };
}

// ... buildEdgeMap function remains the same ...
export function buildEdgeMap(
  rows: number,
  cols: number,
  seed = 42,
): EdgeSet[][] {
  const rand = lcg(seed);
  const map: EdgeSet[][] = Array.from({ length: rows }, () =>
    Array.from({ length: cols }, () => ({
      top: 'flat',
      right: 'flat',
      bottom: 'flat',
      left: 'flat',
    })),
  );
  for (let r = 0; r < rows; r++) {
    for (let c = 0; c < cols; c++) {
      const current = map[r][c];
      if (c < cols - 1) {
        const shape: EdgeShape = rand() < 0.5 ? 'tab' : 'blank';
        current.right = shape;
        map[r][c + 1].left = shape === 'tab' ? 'blank' : 'tab';
      }
      if (r < rows - 1) {
        const shape: EdgeShape = rand() < 0.5 ? 'tab' : 'blank';
        current.bottom = shape;
        map[r + 1][c].top = shape === 'tab' ? 'blank' : 'tab';
      }
    }
  }
  return map;
}

// ... piecePath function remains the same ...
export function piecePath(
  r: number,
  c: number,
  edges: EdgeSet[][],
  pieceW: number,
  pieceH: number,
  knobR = 4,
  tightness = 0.35,
): string {
  const edge = edges[r][c];
  let d = `M ${c * pieceW} ${r * pieceH}`;
  const dx = pieceW / 3;
  const dy = pieceH / 3;
  const t = tightness;
  if (edge.top === 'flat') {
    d += ` h ${pieceW}`;
  } else {
    const sign = edge.top === 'tab' ? -1 : 1;
    d += ` h ${dx / 2} c ${dx * t} 0 ${dx - knobR} ${sign * knobR} ${dx} ${sign * knobR
      } c ${knobR} 0 ${dx - knobR} ${-sign * knobR} ${dx} ${-sign * knobR} h ${dx / 2
      }`;
  }
  if (edge.right === 'flat') {
    d += ` v ${pieceH}`;
  } else {
    const sign = edge.right === 'tab' ? 1 : -1;
    d += ` v ${dy / 2} c 0 ${dy * t} ${sign * knobR} ${dy - knobR} ${sign * knobR
      } ${dy} c 0 ${knobR} ${-sign * knobR} ${dy - knobR} ${-sign * knobR
      } ${dy} v ${dy / 2}`;
  }
  if (edge.bottom === 'flat') {
    d += ` h -${pieceW}`;
  } else {
    const sign = edge.bottom === 'tab' ? 1 : -1;
    d += ` h -${dx / 2} c -${dx * t} 0 -${dx - knobR} ${sign * knobR} -${dx} ${sign * knobR
      } c -${knobR} 0 -${dx - knobR} ${-sign * knobR} -${dx} ${-sign * knobR
      } h -${dx / 2}`;
  }
  if (edge.left === 'flat') {
    d += ` v -${pieceH}`;
  } else {
    const sign = edge.left === 'tab' ? -1 : 1;
    d += ` v -${dy / 2} c 0 -${dy * t} ${sign * knobR} -${dy - knobR} ${sign * knobR
      } -${dy} c 0 -${knobR} ${-sign * knobR} -${dy - knobR} ${-sign * knobR
      } -${dy} v -${dy / 2}`;
  }
  d += ' z';
  return d;
}

/**
 * REPLACEMENT for getRevealOrder.
 * Generates a deterministically random set of revealed pieces
 * based on K (total work) and p (progress).
 */
export function getProgressiveRevealSet(
  rows: number,
  cols: number,
  K: number,
  p: number,
  seed: number,
): Set<number> {
  const total = rows * cols;
  const indices = Array.from({ length: total }, (_, i) => i);

  // 1. Deterministically shuffle all indices
  const rand = lcg(seed);
  let m = indices.length, t, i;
  while (m) {
    i = Math.floor(rand() * m--);
    t = indices[m];
    indices[m] = indices[i];
    indices[i] = t;
  }

  // 2. Clamp K and p to valid ranges
  const clampedK = Math.max(0, Math.min(K, total));
  const clampedP = Math.max(0, Math.min(p, clampedK));

  // 3. Partition indices
  const baseCount = total - clampedK;
  
  // Base pieces (always shown)
  const baseIndices = indices.slice(0, baseCount);
  
  // Progress pieces (shown based on p)
  const progressIndices = indices.slice(baseCount, baseCount + clampedP);

  // 4. Combine and return the set of all shown pieces
  return new Set([...baseIndices, ...progressIndices]);
}

// The getRevealOrder function is no longer needed and can be deleted.