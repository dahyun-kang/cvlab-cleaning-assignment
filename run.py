# -*- encoding:utf-8-*-
import random
import argparse
import unicodedata

def fill_str(input_s="", max_size=70, fill_char=" "):
    # https://frhyme.github.io/python-libs/print_kor_and_en_full_half_width/
    l = 0
    for c in input_s:
        if unicodedata.east_asian_width(c) in ['F', 'W']:
            l+=2
        else:
            l+=1
    return input_s+fill_char*(max_size-l)


class CVLabCleaningAssignment:
    def __init__(self):
        self.all_students = self._init_students()
        self.all_areas = self._init_area()

    def _init_students(self):
        students = []
        with open ('seats.csv') as f:
            for sector in f:
                sector = sector.strip().split(',')
                if len(sector) > 3:  # few-student sectors are ignored
                    students.append(sector)
        return students

    def _init_area(self):
        '''
        Initialize a dictionary of (area -> required number of people)
        '''

        area = dict()
        area["공용 공간 바닥, 공용 공간 책상, 소파 밑 먼지"] = 3
        area["왼쪽 입구쪽 복도, 신발장, 옷장"] = 2
        area["오른쪽 입구쪽 복도, 신발장, 옷장"] = 2
        area["냉장고 정리 (유통기한 지난 것들, 이름 없는 것들)"] = 2
        area["전자레인지 닦기, 소파 먼지 털고 오기"] = 2
        area["파쇄기 비우기/복합기 옆 종이 버리기, 대청소 이후 청소기 잔여물 제거"] = 2
        area["왼/오른쪽 창가 정리, 창가쪽 복도 닦기"] = 2
        return area

    def assign(self):
        assignments = []

        ''' shuffle sectors '''
        random.shuffle(self.all_students)

        for area, students in zip(self.all_areas, self.all_students):
            ''' shuffle students in a sector '''
            random.shuffle(students)

            ''' assign required number of students at the area '''
            num = self.all_areas[area]
            sampled_students = students[:num]
            assignments.append((area, sampled_students))

        ''' hardcoded assignments '''
        assignments.append(("커피머신 청소", ["민교"]))
        assignments.append(("본인 섹터 청소, 개인 공간 청소, 개인 휴지통 비우기", ["나머지"]))

        self.print(assignments)

    def print(self, assignments):
        print(f"\n{args.date} 차 공용 구역 청소 당번입니다.\n")
        for k, v in assignments:
            print(f'{fill_str(k)} | {v}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-date', type=int, help='Random seed in a form of YYYYMM', default=202103)
    args = parser.parse_args()

    ''' set a random seed as an integer YYYYMM '''
    random.seed(args.date)

    CVLabCleaningAssignment().assign()
