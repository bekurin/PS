class Solution {
    public int[][] floodFill(int[][] image, int sr, int sc, int color) {
        int targetColor = image[sr][sc];

        if (targetColor == color) {
            return image;
        }

        int rows = image.length;
        int cols = image[0].length;

        int[] directionRow = {-1, 1, 0, 0};
        int[] directionCol = {0, 0, -1, 1};

        Queue<int[]> queue = new ArrayDeque<>();

        queue.offer(new int[]{sr, sc});
        image[sr][sc] = color;

        while(!queue.isEmpty()) {
            int[] current = queue.poll();
            int row = current[0];
            int col = current[1];

            for(int i = 0; i < 4; i++) {
                int nextRow = row + directionRow[i];
                int nextCol = col + directionCol[i];

                if (nextRow >= 0 && nextRow < rows && nextCol >= 0 && nextCol < cols && image[nextRow][nextCol] == targetColor) {
                    image[nextRow][nextCol] = color;
                    queue.offer(new int[]{nextRow, nextCol});
                }
            }
        }
        return image;
    }
}