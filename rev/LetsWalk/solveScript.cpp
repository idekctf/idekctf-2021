#include <bits/stdc++.h>

using namespace std;

#define ll long long

struct data {
    ll node, weight, state;
    vector < int > array;
};

struct cmp {
    bool operator()(const data &l, const data &r) {
        return l.weight > r.weight;
    }
};

ll w[1000][64], matrix[1000][1000], w1[1000], sum = 0;
int arr[1000], trace[1000], vis1[1000], vis[1000][64], flag[63], n, m;
int path[100000], top;
priority_queue < data, vector < data >, cmp > o;

void read_file_and_init() {
    memset(trace, -1, sizeof(trace));
    for (int i=0; i<1000; i++)
        for (int j=0; j<64; j++)
            w[i][j] = 10000000001;

    FILE *fp;
    fp = fopen("./abc_original.txt", "r");

    int x, y, weight;
    m = 100000;
    n = 1000;

    for (int i=0; i<m; i++) {
        fscanf(fp, "%d %d %d", &x, &y, &weight);

        matrix[x][y] = weight;
        matrix[y][x] = weight;
    }

    arr[82] = 1;    //1
    arr[134] = 2;   //2
    arr[208] = 3;   //3
    arr[671] = 4;   //4
    arr[724] = 5;   //5
    arr[969] = 6;   //6

    fclose(fp);
}

void find_shortest_val() {
    o.push({0, 0, 0, {}});
    w[0][0] = 0;

    while (o.size() != 0) {
        data t = o.top();
        o.pop();

        if (vis[t.node][t.state]) continue;
        vis[t.node][t.state] = 1;

        // cout << t.node + 1 << " " << t.weight << " " << t.state << endl;

        if (t.state == 63) {
            cout << t.weight << " " << t.node << endl;
            for (int i=0; i<t.array.size(); i++)
                cout << t.array[i] << " ";
            cout << endl;
            break;
        }

        for (int i=0; i<n; i++) {
            if (matrix[t.node][i] + t.weight < w[i][t.state] && matrix[t.node][i] != 0 && vis[i][t.state] == 0) {
                if (arr[i] != 0 && (t.state & (1 << (arr[i] - 1))) == 0) {
                    int new_state = (t.state | (1 << (arr[i] - 1)));
                    w[i][new_state] = matrix[t.node][i] + t.weight;

                    vector < int > ar;
                    for (int j=0; j<t.array.size(); j++)
                        ar.push_back(t.array[j]);
                    ar.push_back(i);
                    o.push({i, w[i][new_state], new_state, ar});
                }
                else {
                    w[i][t.state] = matrix[t.node][i] + t.weight;
                    o.push({i, w[i][t.state], t.state, t.array});
                }
            }
        }
    }
}

void save_path(int x, int y) {
    int arr[1000], t = 0;
    memset(arr, 0, sizeof(arr));

    while (y != x) {
        arr[t++] = y;
        y = trace[y];
    }

    for (int i=t-1; i>-1; i--)
        path[top++] = arr[i];
}

void find_shortest_path(int x, int y) {
    memset(trace, -1, sizeof(trace));
    for (int i=0; i<1000; i++) w1[i] = 10000000001;
    memset(vis1, 0, sizeof(vis1));
    while (o.size() != 0) o.pop();

    o.push({x, 0, 0, {}});
    w1[x] = 0;

    while (o.size() != 0) {
        data t = o.top();
        o.pop();

        if (vis1[t.node]) continue;
        vis1[t.node] = 1;

        if (t.node == y) {
            cout << t.weight << endl;
            sum += t.weight;
            save_path(x, y);
            break;
        }

        for (int i=0; i<1000; i++) {
            if (vis1[i] == 0 && w1[t.node] + matrix[t.node][i] < w1[i] && matrix[i][t.node] != 0) {
                w1[i] = w1[t.node] + matrix[t.node][i];
                o.push({i, w1[i], t.state, t.array});
                trace[i] = t.node;
            }
        }
    }
}

int main() {
    path[top++] = 0;
    read_file_and_init();
    find_shortest_val();
    find_shortest_path(0, 82);
    find_shortest_path(82, 969);
    find_shortest_path(969, 208);
    find_shortest_path(208, 134);
    find_shortest_path(134, 724);
    find_shortest_path(724, 671);
    cout << sum << " " << top << endl;

    flag[0] = 105;
    flag[1] = 23;
    flag[2] = 113;
    flag[3] = 211;
    flag[4] = 12;
    flag[5] = 5;
    flag[6] = 39;
    flag[7] = 42;
    flag[8] = 66;
    flag[9] = 160;
    flag[10] = 71;
    flag[11] = 33;
    flag[12] = 18;
    flag[13] = 117;
    flag[14] = 104;
    flag[15] = 240;
    flag[16] = 24;
    flag[17] = 4;
    flag[18] = 166;
    flag[19] = 64;
    flag[20] = 91;
    flag[21] = 219;
    flag[22] = 133;
    flag[23] = 141;
    flag[24] = 169;
    flag[25] = 161;
    flag[26] = 191;
    flag[27] = 141;
    flag[28] = 171;
    flag[29] = 124;
    flag[30] = 171;
    flag[31] = 110;
    flag[32] = 178;
    flag[33] = 249;
    flag[34] = 114;
    flag[35] = 6;
    flag[36] = 103;
    flag[37] = 204;
    flag[38] = 5;
    flag[39] = 51;
    flag[40] = 50;
    flag[41] = 47;
    flag[42] = 71;
    flag[43] = 174;
    flag[44] = 9;
    flag[45] = 39;
    flag[46] = 70;
    flag[47] = 60;
    flag[48] = 111;
    flag[49] = 184;
    flag[50] = 14;
    flag[51] = 75;
    flag[52] = 245;
    flag[53] = 71;
    flag[54] = 67;
    flag[55] = 208;
    flag[56] = 137;
    flag[57] = 217;
    flag[58] = 162;
    flag[59] = 185;
    flag[60] = 174;
    flag[61] = 140;
    flag[62] = 183;

    for (int i=0; i<63; i++)
        cout << path[i] << " ";
    
    return 0;
}