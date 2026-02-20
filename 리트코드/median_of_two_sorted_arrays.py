from typing import List

"""
    [문제 요약] 두 개의 정렬된 배열을 합쳐 중앙값(Median) 찾기
    [해결 방식] 합치기(Merge) -> 정렬(Sort) -> 인덱스 접근
    [주의 사항]
      1. 중앙값은 반드시 '정렬된' 상태에서 계산해야 함.
      2. 전체 길이(N)가 홀수일 때와 짝수일 때의 계산법이 다름.
         - 홀수: middle index 값
         - 짝수: middle과 middle-1 index 값의 평균
    [시간 복잡도] O((M+N) log(M+N)) - 정렬 비용 발생
"""


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()

        n = len(nums1)
        mid = n // 2

        if n % 2 == 0:
            return (nums1[mid - 1] + nums1[mid]) / 2.0

        return float(nums1[mid])


class SolutionV2:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A

        total = len(A) + len(B)
        half = (total + 1) // 2

        left, right = 0, len(A)

        while left <= right:
            i = (left + right) // 2
            j = half - i

            Aleft = A[i - 1] if i > 0 else float("-infinity")
            Aright = A[i] if i < len(A) else float("infinity")
            Bleft = B[j - 1] if j > 0 else float("-infinity")
            Bright = B[j] if j < len(B) else float("infinity")

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    return float(max(Aleft, Bleft))
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2

            elif Aleft > Bright:
                right = i - 1
            else:
                left = i + 1
